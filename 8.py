class Solution:
    def myAtoi(self, str: str) -> int:
        # 1. 先去空格，再找到第一个数字元素，逐个转换
        validNums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        result = 0
        flag = 1  # 正数
        str = str.strip()  # 去掉空白字符
        if not str or str[0] not in validNums + ['+', '-']:  # 字符串为空
            return 0
            # 把对符号的判断提出来会加速，但是代码难看
        for i in range(len(str)):
            if str[i] not in validNums:  # 遇到非数字元素则退出
                if i == 0 and str[i] == '+':
                    continue
                elif i == 0 and str[i] == '-':
                    flag = 0
                    continue
                else:
                    break
            result = result * 10 + int(str[i])
            i += 1
        if not flag:
            result = -result
        result = min(result, 2 ** 31 - 1)
        result = max(result, - 2 ** 31)

        return result

#         # 2. 正则表达式
#         import re

#         # ^代表用^后面的开头，[-+]?表示[-+]可以出现，也可以不出现，也可以只出现1个
#         # \d匹配所有数字，\d+数字后面可以连接无数数字，但不能是其他字符
#         list_s = re.findall(r"^[-+]?\d+", str.strip()) #删除前，后空格。这样容易导致开始碰到字母就为空列表
#         if not list_s:
#             return 0
#         else:
#             num =int(''.join(list_s))
#             if num >2**31 -1:
#                 return 2**31 -1
#             elif num < -2**31:
#                 return -2**31
#             else:
#                 return num