from msg import msg
import sys

def conf():
    print("="*50 + "\n作者是崩坏学园2官方测试服群组2群或者3群的红贽人形哒\n" + "="*50 + "\n")
    sample , info = msg()
    try:
        with open("conf.txt") as conf:
            contents = conf.read()
            contents = eval(contents)
    except FileNotFoundError:
        with open("conf.txt",'a') as conf:
            conf.write(str(sample))
        with open("readme.txt",'a') as conf:
            conf.write(info)
        print("文件conf.txt不存在,已自动生成模板文件，请按照标准填写完成后再次运行本程序")
        print("请仔细阅读说明文档：readme.txt")
        input("按回车键退出")
        sys.exit()
    except SyntaxError:
        input("conf.txt文件异常，删除或者修正\n按回车键退出")
    else:
        return contents


if __name__ == "__main__":
    conf = conf()
    print(conf)