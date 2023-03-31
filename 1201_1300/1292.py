class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """元素和小于等于阈值的正方形最大边长
        1. 前缀和 + 二分, 时间复杂度O(m*n*log(min(m,n))
        先计算矩阵的前缀和, 然后遍历矩阵, 对每一个位置进行二分查找

        2. 前缀和 + 滑动窗口, 时间复杂度O(mn)
        先计算矩阵的前缀和, 然后遍历矩阵, 查找每一个位置的每一个边长是否满足
        """
        # # 1.
        # m, n = len(mat), len(mat[0])
        # # presum
        # presum = [[0]*(n+1) for _ in range(m+1)]
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         presum[i][j] = presum[i][j-1] + presum[i-1][j] + mat[i-1][j-1] - presum[i-1][j-1]
        # # 二分
        # ans = 0
        # for i in range(m):
        #     for j in range(n):
        #         if mat[i][j] > threshold:
        #             continue
        #         l, r = 1, min(i+1, j+1)
        #         while l <= r:
        #             mid = (l + r) // 2
        #             # 正方形端点: (i, j), (i-mid+1, j), (i-mid+1, j-mid+1), (i, j-mid+1)
        #             cursum = presum[i+1][j+1] - presum[i-mid+1][j+1] - presum[i+1][j-mid+1] + \
        #                      presum[i-mid+1][j-mid+1]
        #             if cursum <= threshold:
        #                 l = mid + 1
        #             else:
        #                 r = mid - 1
        #         ans = max(ans, l-1)
        # return ans


        # 2.
        m, n = len(mat), len(mat[0])
        # presum
        presum = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                presum[i][j] = presum[i][j-1] + presum[i-1][j] + mat[i-1][j-1] - presum[i-1][j-1]
        # 滑动窗口
        ans, r = 0, min(m,n)
        for i in range(m):
            for j in range(n):
                for c in range(ans+1, r+1):
                    if i-c+1 < 0 or j-c+1 < 0:
                        break
                    # 正方形端点: (i, j), (i-mid+1, j), (i-mid+1, j-mid+1), (i, j-mid+1)
                    cursum = presum[i+1][j+1] - presum[i-c+1][j+1] - presum[i+1][j-c+1] + \
                             presum[i-c+1][j-c+1]
                    if cursum <= threshold:
                        ans += 1
                    else:
                        break  
        return ans