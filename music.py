import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models
import time

print("作者是崩坏学园2官方测试服群组2群或者3群的红贽人形哒")
# sample = {
#     "SecretId": "您的ID",
#     "SecretKey": "您的Key",
#     "Url": "https://console.cloud.tencent.com/asr/",
#     "suffix": "wav.wav",
#     "start": 1,
#     "end": 10000,
#     "error": 10,
# }
sample = "{" \
         "\n'SecretId': '您的ID'," \
         "\n'SecretKey': '您的Key'," \
         "\n'Url': 'https://console.cloud.tencent.com/asr/'," \
         "\n'suffix': 'wav.wav'," \
         "\n'start': 1," \
         "\n'end': 10000," \
         "\n'error': 10," \
         "\n'language':'16k_zh'," \
         "\n}"
try:
    with open("conf.txt") as conf:
        contents = conf.read()
        contents = eval(contents)
except FileNotFoundError:
    with open("conf.txt",'a') as conf:
        conf.write(str(sample))
    with open("readme.txt",'a') as conf:
        conf.write(str("目前，本程序仅支持URL方式批处理（很明显是为了游戏拆包）\n"
                       "项目开源地址https://github.com/Rcrwrate/tencentcloud-TTS/\n"
                       "编程拉跨，能运行就算成功，重构代码，那是啥，我不知道，我什么都不知道\n\n相关说明：\n"
                       "SecretID/KEY可通过https://console.cloud.tencent.com/cam获取，注意主账号需要开通语音识别https://console.cloud.tencent.com/asr的功能\n"
                       "Url指基础除了数字变动区域以及后缀名以外的全部内容\n"
                       "suffix指代文件名后缀\n"
                       "start指文件名中数字变动区域的起驶数字end反之\n"
                       "error指单次查询能够容忍的错误上限\n"
                       "language指当前语种，具体信息请前往https://cloud.tencent.com/document/product/1093/37823#2.-.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0\n\n"
                       "程序说明：\n"
                       "music.py是主程序，运行之后会产生3个文件：output.txt log.log error.log\n"
                       "第一个是输出，第二个是全过程（不完全），第三个是错误列表\n"
                       "error.py是错误处理文件，目前需要您手动输入错误列表中的taskid获取结果，再将结果复制到output.txt中\n"
                       "once.py是单个处理文件，用于单独处理\n\n"
                       "举例说明：\n"
                       "https://github.com/Rcrwrate/H/name_00001.wav.wav到https://github.com/Rcrwrate/H/name_02345.wav.wav\n"
                       "这是我的音频文件（已经上传到公网能够访问的地方）\n"
                       "此时conf.txt文件应该写成:\n"
                       "{\n"
                       "\t'SecretId': '***',\n"
                       "\t'SecretKey': '***',\n"
                       "\t'Url': 'https://github.com/Rcrwrate/H/name_00001',\n"
                       "\t'suffix': 'wav.wav',\n"
                       "\t'start': 1,\n"
                       "\t'end': 2345,\n"
                       "\t'error':10,\n"
                       "}\n\n"
                       "更多说明请前往https://github.com/Rcrwrate/TTS-Tencentcloud/wiki\n"))
    print("文件conf.txt不存在,已自动生成模板文件，请按照标准填写完成后再次运行本程序")
    print("请仔细阅读说明文档：readme.txt")
    input("按回车键退出")
except SyntaxError:
    input("conf.txt文件异常，删除或者修正\n按回车键退出")
else:
    for i in range(contents["start"], contents["end"]+1):
        cent = int((float(i) - float(contents["start"]) + 1) / (float(contents["end"]) - float(contents["start"])) * 100 )
        if i < 10:
            i = "0000" + str(i)
        elif 10 <= i and i < 100:
            i = "000" + str(i)
        elif 100 <= i and i < 1000:
            i = "00" + str(i)
        else:
            i = "0" + str(i)
        url = str(contents['Url']) + i + '.' + str(contents['suffix'])
        num = int(float(cent)/2)
        pre = '\r{}%:{}'.format(cent,'#'*num)
        print('{}:  {}正在准备中'.format(pre,i),end='',flush=True)
        with open('log.log','a') as log:
            log.write('='*16+ i + '='*16 +'\n')
            with open('output.txt', 'a') as f:
                f.write(i+"."+str(contents['suffix'])+"\n")
                try:
                    cred = credential.Credential(contents['SecretId'], contents['SecretKey'])
                    httpProfile = HttpProfile()
                    httpProfile.endpoint = "asr.tencentcloudapi.com"

                    clientProfile = ClientProfile()
                    clientProfile.httpProfile = httpProfile
                    client = asr_client.AsrClient(cred, "", clientProfile)

                    req = models.CreateRecTaskRequest()
                    params = {
                        "EngineModelType": contents["language"],
                        "ChannelNum": 1,
                        "ResTextFormat": 0,
                        "SourceType": 0,
                        "Url": url
                    }
                    req.from_json_string(json.dumps(params))

                    resp = client.CreateRecTask(req)
                    # print(resp.to_json_string())
                    print('{}:  {}已提交    '.format(pre,i),end='',flush=True)
                except TencentCloudSDKException as err:
                    print(err)
                try:
                    strs = resp.to_json_string()
                    TID = int(strs[20:30])
                except NameError as err:
                    print("conf.txt输入有误")
                null = 0
                check = 1
                while check != 2:
                    null = null + 1
                    time.sleep(2)
                    try:
                        cred = credential.Credential(contents['SecretId'], contents['SecretKey'])
                        httpProfile = HttpProfile()
                        httpProfile.endpoint = "asr.tencentcloudapi.com"

                        clientProfile = ClientProfile()
                        clientProfile.httpProfile = httpProfile
                        client = asr_client.AsrClient(cred, "", clientProfile)

                        req = models.DescribeTaskStatusRequest()
                        params = {
                            "TaskId": TID
                        }
                        req.from_json_string(json.dumps(params))

                        resp = client.DescribeTaskStatus(req)
                        # print(resp.to_json_string())
                        recognition_text = resp.to_json_string()
                        log.write(recognition_text+"\n")
                        check = eval(recognition_text)['Data']['Status']
                        if null >= contents['error']:
                            with open('error.log','a') as errr:
                                errr.write("ID:{}  TaskId:{}\n".format(i,TID))
                            print("\n error! ID:{}  TaskId:{} \n".format(i,TID))
                            break
                        if str(check) == "3":
                            with open('error.log','a') as errr:
                                errr.write("ID:{}  TaskId:{}\n".format(i,TID))
                            print("\n error! ID:{}  TaskId:{}  系统无法转义 \n".format(i,TID))
                            break
                    except TencentCloudSDKException as err:
                        print(err)
                    except NameError as err:
                        print("conf.txt输入有误")
                print('{}:  {}已完成    '.format(pre,i),end='',flush=True)
                message = eval(recognition_text)['Data']['Result']
                f.write(message+"\n")
input("按回车键退出")
