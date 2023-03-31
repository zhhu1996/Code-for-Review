class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        """与目标颜色间的最短距离
        1. dp
        带维度单串, 位置i必取, O(1)个子问题, 时间复杂度O(n)
        left[i][k]: colors[0..i]上距离最近的k元素的索引
        right[i][k]: colors[i..n-1]上距离最近的k元素的索引
        """
        n = len(colors)
        left, right = [[-1]*3 for _ in range(n)], [[n]*3 for _ in range(n)]
        for i in range(n):
            for j in range(3):
                if j == colors[i]-1:
                    left[i][j] = i
                elif i > 0:
                    left[i][j] = left[i-1][j]
        for i in range(n-1, -1, -1):
            for j in range(3):
                if j == colors[i]-1:
                    right[i][j] = i
                elif i < n-1:
                    right[i][j] = right[i+1][j]
        res = []
        for q in queries:
            index, target = q[0], q[1]
            l_i = left[index][target-1]
            r_i = right[index][target-1]
            ans = -1
            if l_i == -1 and r_i == n:
                ans = -1
            elif l_i == -1:
                ans = r_i-index
            elif r_i == n:
                ans = index-l_i
            else:
                ans = min(index-l_i, r_i-index)
            res.append(ans)
        return res