class Solution:
    def myPow(self, x: float, n: int) -> float:
        """考虑多种情况
        1. 常规解法
        2. 二分法快速求解
        """

        # if x == 0 and n < 0:
        #     return 0.0
        #
        # absN = n
        # if n < 0:
        #     absN = -n
        # res = 1
        # for i in range(absN):
        #     res *= x
        # if n < 0:
        #     res = 1.0 / res
        # return res

        def getPow(x, n):
            if n == 0:
                return 1
            if n % 2 == 0:
                return getPow(x, n//2) ** 2
            else:
                return getPow(x, n//2) ** 2 * x

        if x == 0 and n < 0:
            return 0.0
        if n >= 0:
            return getPow(x, n)
        else:
            return getPow(1 / x, -n)