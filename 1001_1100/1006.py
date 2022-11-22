class Solution:
    def clumsy(self, N: int) -> int:
        """笨阶乘
        1. 暴力

        2. 规律
        """
        # # 方法1
        # res = 0
        # flag = 1
        # origin = [0, 1, 2, 6]
        # if N < 4:
        #     return origin[N]
        # while N >= 4:
        #     if flag:
        #         res += N * (N - 1) // (N - 2) + N - 3
        #         flag = 0
        #     else:
        #         res -= N * (N - 1) // (N - 2) - (N - 3)
        #     N -= 4
        # return res - origin[N]

        # 方法2
        origin = [0, 1, 2, 6, 7]
        if N <= 4:
            return origin[N]
        if N % 4 == 0:
            return N + 1
        elif N % 4 == 3:
            return N - 1
        else:
            return N + 2
