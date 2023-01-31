class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #         # 1. 库函数
        #         num1 = int(num1)
        #         num2 = int(num2)

        #         return str(num1 * num2)

        # 2. 计算每一位数的相乘结果，然后进行累加
        # 有0的情况
        if num1 == "0" or num2 == "0":
            return "0"

        res = []
        n1, n2 = len(num1), len(num2)
        # 计算每一位数的相乘结果
        for i in range(n2 - 1, -1, -1):
            temp = []
            a = int(num2[i])
            carry = 0
            for j in range(n1 - 1, -1, -1):
                num = a * int(num1[j]) + carry
                temp.append(num % 10)
                carry = num // 10
            if carry:  # 注意进位
                temp.append(carry)
            temp = temp[::-1]
            # 补0
            for k in range(n2 - 1 - i):
                temp.append(0)
            self.cal(res, temp)

        return ''.join(str(i) for i in res)

        # # 3. 模拟数字乘法
        # if num1 == '0' or num2 == '0':
        #     return '0'
        # res = 0
        # base = 1
        # for i in range(len(num2)-1, -1, -1):
        #     res += int(num1) * int(num2[i]) * base
        #     base = base * 10
        # return str(res)

    def cal(self, res, temp):
        # 实现两个数组的相加：首先要对齐两个数组，然后逐元素相加
        if len(res) <= len(temp):
            for i in range(len(temp) - len(res)):
                res.insert(0, 0)
        else:
            for i in range(len(res) - len(temp)):
                temp.insert(0, 0)
        n = len(res)
        carry = 0
        for i in range(n - 1, -1, -1):
            t = res[i] + temp[i] + carry
            res[i] = t % 10
            carry = t // 10
        if carry == 1:
            res.insert(0, 1)
