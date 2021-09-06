# tencentcloud-TTS
## [![ALL](https://github.com/Rcrwrate/TTS-Tencentcloud/actions/workflows/all.yml/badge.svg)](https://github.com/Rcrwrate/TTS-Tencentcloud/actions/workflows/all.yml)

### 编程拉跨，能运行就算成功，重构代码，那是啥，我不知道，我什么都不知道
### 本程序自用+练练手（有问题在issues里问，能解答我就解答，毕竟我也是彩笔，一个actions弄了我老半天，绝了
## 目前，本程序仅支持URL方式批处理（很明显是为了游戏拆包）

软件下载：

自动化编译结果：[windows](https://github.com/Rcrwrate/TTS-Tencentcloud/tree/main/dist) // [ubuntu](https://github.com/Rcrwrate/TTS-Tencentcloud/tree/main/dist)

手动编译结果：[windows](https://github.com/Rcrwrate/TTS-Tencentcloud/releases)

### 程序说明：
music.py是主程序，运行之后会产生3个文件：output.txt log.log error.log

第一个是输出，第二个是全过程（不完全），第三个是错误列表

error.py是错误处理文件，目前需要您手动输入错误列表中的taskid获取结果，再将结果复制到output.txt中

once.py是单个处理文件，用于单独处理

### 相关说明：
SecretID/KEY可通过[https://console.cloud.tencent.com/cam](https://console.cloud.tencent.com/cam)获取，注意主账号需要开通[语音识别](https://console.cloud.tencent.com/asr)的功能

Url指基础除了数字变动区域以及后缀名以外的全部内容

suffix指代文件名后缀

start指文件名中数字变动区域的起驶数字，end反之

error指单次查询能够容忍的错误上限

### 举例说明：
https://github.com/Rcrwrate/H/name_00001.wav.wav到https://github.com/Rcrwrate/H/name_02345.wav.wav

这是我的音频文件（已经上传到公网能够访问的地方）

此时conf.txt文件应该写成:

`{
    'SecretId': '***',
    'SecretKey': '***',
    'Url': 'https://github.com/Rcrwrate/H/name_',
    'suffix': 'wav.wav',
    'start': 1,
    'end': 2345,
    'error':10,
    }`

# 更多说明请前往https://github.com/Rcrwrate/TTS-Tencentcloud/wiki
