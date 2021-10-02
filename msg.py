def msg():
    sample = '''{
'SecretId': '您的ID',
'SecretKey': '您的Key',
'Url': 'https://console.cloud.tencent.com/asr/',
'suffix': 'wav.wav',
'start': 1,
'end': 10000,
'error': 10,
'language':'16k_zh',
}
'''
    info = '''
目前，本程序仅支持URL方式批处理（很明显是为了游戏拆包）
项目开源地址https://github.com/Rcrwrate/tencentcloud-TTS/
编程拉跨，能运行就算成功，重构代码，那是啥，我不知道，我什么都不知道

相关说明：
SecretID/KEY可通过https://console.cloud.tencent.com/cam获取，注意主账号需要开通语音识别https://console.cloud.tencent.com/asr的功能
Url指基础除了数字变动区域以及后缀名以外的全部内容
suffix指代文件名后缀
start指文件名中数字变动区域的起驶数字end反之
error指单次查询能够容忍的错误上限
language指当前语种，具体信息请前往https://cloud.tencent.com/document/product/1093/37823#2.-.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0

程序说明：
music.py是主程序，运行之后会产生3个文件：output.txt log.log error.log
第一个是输出，第二个是全过程（不完全），第三个是错误列表
error.py是错误处理文件，目前需要您手动输入错误列表中的taskid获取结果，再将结果复制到output.txt中
once.py是单个处理文件，用于单独处理

举例说明：
https://github.com/Rcrwrate/H/name_00001.wav.wav到https://github.com/Rcrwrate/H/name_02345.wav.wav
这是我的音频文件（已经上传到公网能够访问的地方）
此时conf.txt文件应该写成:
{
	'SecretId': '***',
	'SecretKey': '***',
	'Url': 'https://github.com/Rcrwrate/H/name_00001',
	'suffix': 'wav.wav',
	'start': 1,
	'end': 2345,
	'error':10,
}

更多说明请前往https://github.com/Rcrwrate/TTS-Tencentcloud/wiki
目前，本程序仅支持URL方式批处理（很明显是为了游戏拆包）
项目开源地址https://github.com/Rcrwrate/tencentcloud-TTS/
编程拉跨，能运行就算成功，重构代码，那是啥，我不知道，我什么都不知道

相关说明：
SecretID/KEY可通过https://console.cloud.tencent.com/cam获取，注意主账号需要开通语音识别https://console.cloud.tencent.com/asr的功能
Url指基础除了数字变动区域以及后缀名以外的全部内容
suffix指代文件名后缀
start指文件名中数字变动区域的起驶数字end反之
error指单次查询能够容忍的错误上限
language指当前语种，具体信息请前往https://cloud.tencent.com/document/product/1093/37823#2.-.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0

程序说明：
music.py是主程序，运行之后会产生3个文件：output.txt log.log error.log
第一个是输出，第二个是全过程（不完全），第三个是错误列表
error.py是错误处理文件，目前需要您手动输入错误列表中的taskid获取结果，再将结果复制到output.txt中
once.py是单个处理文件，用于单独处理

举例说明：
https://github.com/Rcrwrate/H/name_00001.wav.wav到https://github.com/Rcrwrate/H/name_02345.wav.wav
这是我的音频文件（已经上传到公网能够访问的地方）
此时conf.txt文件应该写成:
{
	'SecretId': '***',
	'SecretKey': '***',
	'Url': 'https://github.com/Rcrwrate/H/name_00001',
	'suffix': 'wav.wav',
	'start': 1,
	'end': 2345,
	'error':10,
}

更多说明请前往https://github.com/Rcrwrate/TTS-Tencentcloud/wiki
目前，本程序仅支持URL方式批处理（很明显是为了游戏拆包）
项目开源地址https://github.com/Rcrwrate/tencentcloud-TTS/
编程拉跨，能运行就算成功，重构代码，那是啥，我不知道，我什么都不知道

相关说明：
SecretID/KEY可通过https://console.cloud.tencent.com/cam获取，注意主账号需要开通语音识别https://console.cloud.tencent.com/asr的功能
Url指基础除了数字变动区域以及后缀名以外的全部内容
suffix指代文件名后缀
start指文件名中数字变动区域的起驶数字end反之
error指单次查询能够容忍的错误上限
language指当前语种，具体信息请前往https://cloud.tencent.com/document/product/1093/37823#2.-.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0

程序说明：
music.py是主程序，运行之后会产生3个文件：output.txt log.log error.log
第一个是输出，第二个是全过程（不完全），第三个是错误列表
error.py是错误处理文件，目前需要您手动输入错误列表中的taskid获取结果，再将结果复制到output.txt中
once.py是单个处理文件，用于单独处理

举例说明：
https://github.com/Rcrwrate/H/name_00001.wav.wav到https://github.com/Rcrwrate/H/name_02345.wav.wav
这是我的音频文件（已经上传到公网能够访问的地方）
此时conf.txt文件应该写成:
{
	'SecretId': '***',
	'SecretKey': '***',
	'Url': 'https://github.com/Rcrwrate/H/name_00001',
	'suffix': 'wav.wav',
	'start': 1,
	'end': 2345,
	'error':10,
}

更多说明请前往https://github.com/Rcrwrate/TTS-Tencentcloud/wiki

    '''
    return sample,info

def console():
	t1 = '''
指令(指令输入字首即可):
h | help\t\t\t\t\t\t--- 显示说明 (显示此讯息)
c | conf\t\t\t\t\t\t--- 显示配置文件
q | quit\t\t\t\t\t\t--- 退出脚本
r | run\t\t\t\t\t\t\t--- 按照配置直接运行
i <id> | id <id> \t\t\t\t\t--- 基于配置，通过单个id进行单次解析
u <url> | url <url> \t\t\t\t\t--- 对单个url进行单次解析
d | delete\t\t\t\t\t\t--- 删除所有中间产生的临时文件(即output.txt除外)
'''
	print(t1)
	return t1


if __name__ == '__main__':
	console()