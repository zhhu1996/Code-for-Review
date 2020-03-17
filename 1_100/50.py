class Solution:
    def myPow(self, x: float, n: int) -> float:
        # # 1. 偷懒
        # return x**n

        #         # 2. 简单递归堆栈溢出了
        #         def getPow(x, n):
        #             if n == 0:
        #                 return 1

        #             return x * getPow(x, n-1)

        #         if n >= 0:
        #             return getPow(x, n)

        #         else:
        #             return 1 / getPow(x, -n)

        # 3. 快速递归，即通过x^n/2计算x^n
        def getPow(x, n):
            if n == 0:
                return 1
            if n % 2 == 0:
                return getPow(x, n // 2) ** 2
            else:
                return getPow(x, n // 2) ** 2 * x

        if n >= 0:
            return getPow(x, n)
        else:
            return getPow(1 / x, -n)