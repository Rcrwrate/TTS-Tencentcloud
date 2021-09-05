import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models

print("作者是崩坏学园2官方测试服群组2群或者3群的红贽人形哒")
sample = "{" \
         "\n'SecretId': '您的ID'," \
         "\n'SecretKey': '您的Key'," \
         "\n'Url': 'https://console.cloud.tencent.com/asr/'," \
         "\n'suffix': 'wav.wav'," \
         "\n'start': 1," \
         "\n'end': 10000," \
         "\n'error': 10," \
         "\n}"
try:
    with open("conf.txt") as conf:
        contents = conf.read()
        contents = eval(contents)
except FileNotFoundError:
    with open("conf.txt", 'a') as conf:
        conf.write(str(sample))
    with open("readme.txt",'a') as conf:
        conf.write(str("目前，本程序仅支持URL方式批处理（很明显是为了游戏拆包）\n"
                       "项目开源地址https://github.com/Rcrwrate/tencentcloud-TTS/\n"
                       "编程拉跨，能运行就算成功，重构代码，那是啥，我不知道，我什么都不知道\n\n相关说明：\n"
                       "SecretID/KEY可通过https://console.cloud.tencent.com/cam获取，注意主账号需要开通语音识别https://console.cloud.tencent.com/asr的功能\n"
                       "Url指基础除了数字变动区域以及后缀名以外的全部内容\n"
                       "suffix指代文件名后缀\n"
                       "start指文件名中数字变动区域的起驶数字end反之\n"
                       "error指单次查询能够容忍的错误上限\n\n"
                       "程序说明：\n"
                       "music.py是主程序，运行之后会产生3个文件：output.txt log.log error.log\n"
                       "第一个是输出，第二个是全过程（不完全），第三个是错误列表\n"
                       "error.py是错误处理文件，目前需要您手动输入错误列表中的taskid获取结果，再将结果复制到output.txt中\n\n"
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
                       "}\n"))
    print("文件conf.txt不存在,已自动生成模板文件，请按照标准填写完成后再次运行本程序")
    print("请仔细阅读说明文档：readme.txt")
    input("按回车键退出")
else:
    TID = 1
    null = 0
    while TID:
        TID = int(input('Plz input error TID：'))
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
            recognition_text = resp.to_json_string()
            Result = eval(recognition_text)['Data']['Result']
            print(Result)
        except TencentCloudSDKException as err:
            print(err)
        except NameError as err:
            print("conf.txt输入有误")
