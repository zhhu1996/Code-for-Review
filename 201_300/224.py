class Solution:
    def calculate(self, s: str) -> int:
        """基本计算器
        方法1: 一个数据堆栈，一个符号堆栈
        """
        if not s:
            return 0

        def rm_blank(s):
            result = []
            for i in range(len(s)):
                if s[i] != ' ':
                    result.append(s[i])
            return "".join(result)

        def find_next_num(s, start, next=True):
            cur = 0
            if next:
                i = start + 1
            else:
                i = start
            cur = 0
            while i < len(s):
                if s[i] in '0123456789':
                    cur = cur * 10 + int(s[i])
                    i += 1
                else:
                    break
            return cur, i - start

        def get_sequence(s):
            result = []
            i = 0
            while i < len(s):
                if s[i] == ' ':
                    i += 1
                elif s[i] == '(' or s[i] == ')':
                    result.append(s[i])
                    i += 1
                elif s[i] == '+' or s[i] == '-':
                    j = i - 1
                    if i == 0:
                        if s[i+1] == '(':
                            result.append(s[i])
                            i += 1
                        else:
                            signal = s[i]
                            cur, offset = find_next_num(s, i)
                            i += offset
                            if signal == '+':
                                result.append(str(cur))
                            else:
                                result.append(str(-cur))
                            continue
                    while j >= 0:
                        if s[j] == ' ':
                            j -= 1
                        elif s[j] in '(+-':
                            signal = s[i]
                            cur, offset = find_next_num(s, i)
                            i += offset
                            if signal == '+':
                                result.append(str(cur))
                            else:
                                result.append(str(-cur))
                            break
                        else:  # num or )
                            result.append(str(s[i]))
                            i += 1
                            break
                else:  # num
                    cur, offset = find_next_num(s, i, False)
                    i += offset
                    result.append(str(cur))

            return result

        def basic_op(sign, nums, op):
            sign.pop()
            b = nums.pop()
            a = nums.pop()
            if op == '+':
                nums.append(a+b)
            elif op == '-':
                nums.append(a-b)

        sign = []
        nums = []
        s = rm_blank(s)
        ops = get_sequence(s)
        for i in range(len(ops)):
            c = ops[i]
            if c == ' ':
                continue
            elif c == '(':
                sign.append(c)
            elif c == ')':
                while sign[-1] != '(':
                    basic_op(sign,nums,sign[-1])
                sign.pop()
            elif c in '+-':
                while sign and sign[-1] in '+-':
                    basic_op(sign,nums,sign[-1])
                sign.append(c)
            else: # num
                nums.append(int(c))
        while sign and len(nums) >= 2:
            basic_op(sign,nums,sign[-1])
        if sign:
            flag = sign.pop()
            data = nums.pop()
            if flag == '+':
                return data
            else:
                return -data
        else:
            return nums[-1]