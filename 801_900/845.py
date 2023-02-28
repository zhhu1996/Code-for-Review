class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        """数组中的最长山脉
        1. 区间dp, 时间复杂度O(n^2), 超时
        dp[i][j]表示arr[i..j]是否是山脉数组
        i.  nums[i] < nums[i+1] && nums[j-1] > nums[j]
        dp[i][j] = dp[i+1][j-1]
        ii. nums[i] < nums[i+1]
        dp[i][j] = dp[i+1][j]
        iii.nums[j-1] > nums[j]
        dp[i][j] = dp[i][j-1]
        iv. else
        dp[i][j] = 0

        2. 单串dp, 时间复杂度O(n)
        left[i]表示以i结尾的最长递增子序列长度, right[i]表示以i开头的最长递减子序列长度
        枚举山顶元素, 向左右扩展即可得到山峰数组长度

        3. 双指针, 时间复杂度O(n)
        循环不变体: i作为迭代变量, arr[i..j]是山脉子数组
        """
        # # 2.
        # n = len(arr)
        # left, right = [1]*n, [1]*n
        # res = 0
        # for i in range(1, n):
        #     left[i] = left[i-1]+1 if arr[i] > arr[i-1] else 1
        # for j in range(n-2, -1, -1):
        #     right[j] = right[j+1]+1 if arr[j] > arr[j+1] else 1
        # for i in range(n):
        #     if left[i] > 1 and right[i] > 1:
        #         cur = left[i] + right[i] - 1
        #         res = max(res, cur)
        # return res

        # 3.
        n = len(arr)
        if n <= 2: return 0
        i, j = 0, -1
        res = 0
        while i + 2 < n:
            j = i+1
            if arr[i] < arr[i+1]:
                while j+1 < n and arr[j] < arr[j+1]:
                    j += 1
                if j+1 < n and arr[j] > arr[j+1]:
                    while j+1 < n and arr[j] > arr[j+1]:
                        j += 1
                    res = max(res, j-i+1)
            i = j
        return res