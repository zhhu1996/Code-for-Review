class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        """
        1. dp, 时间复杂度O(n)
        带维度单串, 位置i必取, O(1)个子问题
        dp[i][j]: 到达点i的赛道j需要的最少次数
        1) 上一个状态 -> 当前状态
        2) 当前状态横向更新

        2. 贪心, 时间复杂度O(n)
        不遇到障碍就一直走, 遇到障碍就跳到离下一块障碍最远的赛道
        """
        # # 1.
        # n = len(obstacles)
        # # dp
        # dp = [[float('inf')]*3 for _ in range(n)]
        # dp[0][0], dp[0][1], dp[0][2] = 1, 0, 1
        # for i in range(1, n):
        #     mincnt = float('inf')
        #     # 1) 上一个状态 -> 当前状态
        #     for j in range(3):
        #         if obstacles[i]-1 == j:
        #             dp[i][j] = float('inf')
        #         else:
        #             dp[i][j] = dp[i-1][j]
        #         mincnt = min(mincnt, dp[i][j])
        #     # 2) 当前状态横向更新
        #     for j in range(3):
        #         if obstacles[i]-1 != j:
        #             dp[i][j] = min(dp[i][j], mincnt+1)
        # return min(dp[n-1])


        # 2.
        ans, i, j, n = 0, 0, 1, len(obstacles)
        # i表示青蛙的横坐标, j表示纵坐标
        while i < n-1:
            if obstacles[i+1]-1 != j:
                i += 1
                continue
            # 寻找下跳能走最远的赛道
            other = (j+1) % 3
            another = (j+2) % 3
            other_cnt, another_cnt = 0, 0
            for k in range(i, n):
                if obstacles[k]-1 == other:
                    break
                else:
                    other_cnt += 1
            for k in range(i, n):
                if obstacles[k]-1 == another:
                    break
                else:
                    another_cnt += 1
            j = (other if other_cnt > another_cnt else another)
            i += max(other_cnt, another_cnt) - 1
            ans += 1
        return ans