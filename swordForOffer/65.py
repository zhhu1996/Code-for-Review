class Solution:
    def add(self, a: int, b: int) -> int:
        """不用加减乘除做加法
        通过位运算来实现
        1. 每位不考虑进位，相加: 异或操作
        2. 计算进位: 与操作，并左移1位
        3. 重复1、2操作
        """
        # allSum, carry = 0, 0
        # while b != 0:
        #     allSum = a ^ b
        #     carry = (a & b) << 1
        #     a = allSum
        #     b = carry
        # return allSum

        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)