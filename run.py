from core import Core, get
from msg import msg, console
from conf import conf
from other import delete_all, delete
import sys
import re


def main():
    return 0


conf = conf()
test = Core()
Core.change_info(self=test, contents=conf)
# Core.debug(self=test)
console()
inputs = re.split('\\s+', get('>').strip())
while True:
    if inputs[0].startswith('q'):
        sys.exit()
    elif inputs[0].startswith('h'):
        console()
    elif inputs[0].startswith('c'):
        test.debug()
    elif inputs[0].startswith('r'):
        delete("temp.log")
        test.mult_input_id()
        test.mult_output_str()
        delete("temp.log")
    elif inputs[0].startswith('i'):
        try:
            test.id = int(inputs[1])
        except Exception as err:
            print(err)
            print("请按照格式正确输入")
        else:
            TID = test.once_input()
            test.once_output(TID=TID)
        test.id = 0
    elif inputs[0].startswith('u'):
        url = inputs[1]
        TID = Core.once_input(self=test, url=url)
        print("\n")
        print(Core.once_output(self=test, TID=TID))

    elif inputs[0].startswith('d'):
        delete_all()
        print("已删除所有临时文件")
    inputs = re.split('\\s+', get('>').strip())

if __name__ == "__main__":
    main()
