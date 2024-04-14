class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        """恰好移动k步到某一位置的方法数目
        1. 记忆化搜索

        2. dp
        双串, 位置i必取, O(1)个子问题
        求组合数C(k, a), a=(diff+k)//2
        """
        # # 1.
        # self.ans = {}

        # def f(pos, left):
        #     # 位置pos走left步到达endPos的方法数
        #     if (pos, left) in self.ans:
        #         return self.ans[(pos, left)]
        #     if abs(pos - endPos) > left:
        #         return 0
        #     if left == 0:
        #         return 1
        #     val = (f(pos-1, left-1) + f(pos+1, left-1)) % (10**9 + 7)
        #     self.ans[(pos, left)] = val
        #     return val

        # return f(startPos, k)


        # 2. 
        if startPos > endPos:
            startPos, endPos = endPos, startPos
        d = endPos - startPos
        if (d + k) % 2 != 0 or d > k:
            return 0
        c = [[0]*(k+1) for _ in range(k+1)]
        for i in range(k+1):
            c[i][0] = 1
            for j in range(1, i+1):
                c[i][j] = (c[i-1][j] + c[i-1][j-1]) % (10**9+7)
        return c[k][(d+k)//2]