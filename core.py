import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import (
    TencentCloudSDKException,
)
from tencentcloud.asr.v20190614 import asr_client, models
import time


class Core:
    def __init__(
        self,
        SecretId=0,
        SecretKey=0,
        Url=0,
        suffix=0,
        start=0,
        end=0,
        error=0,
        language=0,
    ):
        self.SecretId = SecretId
        self.SecretKey = SecretKey
        self.Url = Url
        self.suffix = suffix
        self.start = start
        self.end = end
        self.error = error
        self.language = language
        self.id = self.start
        self.temp = ""
        self.error_count = 0
        global null
        null = 0

    def change_info(self, contents):
        self.SecretId = contents["SecretId"]
        self.SecretKey = contents["SecretKey"]
        self.Url = contents["Url"]
        self.suffix = contents["suffix"]
        self.start = contents["start"]
        self.end = contents["end"]
        self.error = contents["error"]
        self.language = contents["language"]


    def debug(self):
        print(
            "="*42 +
            "\nSecretId:\t" + str(self.SecretId) +
            "\nSecretKey:\t" + str(self.SecretKey) +
            "\nUrl:\t\t" + str(self.Url) +
            "\nsuffix:\t\t" + str(self.suffix) +
            "\nstart:\t\t" + str(self.start) +
            "\nend:\t\t" + str(self.end) +
            "\nerror:\t\t" + str(self.error) +
            "\nlanguage:\t" + str(self.language) +
            "\nid:\t\t" + str(self.id) + "\n" + "="*42 + "\n"
        )

    def log(self, item, type="log"):#日志输出
        if type == "log": #懒得改了，就这样吧
            with open("log.log", "a") as log:
                log.write("=" * 16 + str(self.id) + "=" * 16 + "\n")
                log.write(str(item) + "\n")
        elif type == "out":
            with open("output.txt", "a") as out:
                out.write(str(self.id) + "." + str(self.suffix) + "\n")
                out.write(str(item) + "\n")
        elif type == "temp":
            with open("temp.log", "a") as temp:
                temp.write(str(self.id) + ":" + str(item)+"\n")
        elif type == "error":
            with open("error.log", "a") as error:
                error.write("=" * 16 + str(self.id) + "=" * 16 + "\n")
                error.write(str(item)+"\n")
        
    def error_check(self):
        if self.error_count >= self.error:
            import sys
            print("\n\n异常过多，请检查文件!")
            input("输入回车退出程序:")
            sys.exit(1)

    def once_input(self,url=""):#单次查询请求模块
        self.error_check()
        if url == "":
            url = str(self.Url) + str(self.id) + '.' + str(self.suffix)
        else:
            self.id = "单次测试"
        try:
            cred = credential.Credential(self.SecretId, self.SecretKey)
            httpProfile = HttpProfile()
            httpProfile.endpoint = "asr.tencentcloudapi.com"

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = asr_client.AsrClient(cred, "", clientProfile)

            req = models.CreateRecTaskRequest()
            params = {
                "EngineModelType": self.language,
                "ChannelNum": 1,
                "ResTextFormat": 0,
                "SourceType": 0,
                "Url": url
            }
            req.from_json_string(json.dumps(params))

            resp = client.CreateRecTask(req)
            # print(resp.to_json_string())
            print('{}已提交            '.format(self.temp),end='',flush=True)
        except TencentCloudSDKException as err:
            self.log(item=err,type="error")
            print("\n" + str(err) + "\n")
            self.error_count += 1
        else:
            strs = resp.to_json_string()
            self.log(item=strs,type="log")
            TID = eval(strs)['Data']['TaskId']
            self.log(item=TID,type="temp")
            return TID

    def mult_input_id(self):#核心批量生成请求模块
        for i in range(self.start, self.end+1):
            cent = int((float(i) - float(self.start) + 1) / (float(self.end) - float(self.start)) * 100 )
            if i < 10:
                i = "0000" + str(i)
            elif 10 <= i and i < 100:
                i = "000" + str(i)
            elif 100 <= i and i < 1000:
                i = "00" + str(i)
            else:
                i = "0" + str(i)
            self.id = i
            num = int(float(cent)/2)
            pre = '\r{}%:{}'.format(cent,'#'*num)
            self.temp = '{}:  {}'.format(pre,i)
            print('{}正在准备中'.format(self.temp),end='',flush=True)
            self.once_input()

    def once_output(self,strtid=":",TID=0):
        if TID == 0:
            Temp = strtid.split(":")
            self.id = Temp[0]
            TID = int(Temp[1])
        else:
            self.id = "单次测试"
            TID = TID
        Status = 0
        check = 0
        while Status != 2:
            check += 1
            try:
                cred = credential.Credential(self.SecretId, self.SecretKey)
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
                self.log(item=recognition_text,type="log")
                Status = eval(recognition_text)['Data']['Status']
                if check >= self.error:
                    self.log(item="ID:{}  TaskId:{}\n".format(self.id,TID),type="error")
                    print("\n error! ID:{}  TaskId:{} \n".format(self.id,TID))
                    break
                if str(Status) == "3":
                    self.log(item="ID:{}  TaskId:{}\n".format(self.id,TID),type="error")
                    print("\n error! ID:{}  TaskId:{}  系统无法转义 \n".format(self.id,TID))
                    break
                if str(Status) == "2":
                    message = eval(recognition_text)['Data']['Result']
                    self.log(item=message,type="out")
                    return message
            except TencentCloudSDKException as err:
                self.log(item=err,type="error")
                print(err)
            except Exception as err:
                self.log(item=err,type="error")
                print(err)
            time.sleep(2)

    def mult_output_str(self):
        with open("temp.log","r") as fn:
            for lines in fn.readlines():
                self.once_output(strtid=lines)

if __name__ == "__main__":
    from conf import conf

    conf = conf()
    test = Core()
    Core.change_info(self=test, contents=conf)
    Core.debug(self=test)

    # Core.mult_input_id(self=test)
    # Core.once_output(self=test,strtid="00007:1483001931")
    # Core.mult_output_str(self=test)

    #独立URL测试
    url= "http://ys-o.ys168.com/617723448/615738753/u562267437JPHIhVRtk8c9/Cv_Partner_00762.wav.wav"
    TID = Core.once_input(self=test,url=url)
    print(Core.once_output(self=test,TID=TID))
