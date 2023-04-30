class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """找出游戏的获胜者
        1. 循环数组模拟, 时间复杂度O(n^2)

        2. dp, 时间复杂度O(n)
        f[i][m] = (f[i-1][m] + m) % i
        """
        # # 1.
        # arr = [i for i in range(n)]
        # index = 0
        # while len(arr) > 1:
        #     lth = len(arr)
        #     index = (index + k - 1) % lth
        #     arr.pop(index)
        # return arr[-1]+1


        # 2.
        p = 0
        for i in range(2, n+1):
            p = (p + k) % i
        return p + 1