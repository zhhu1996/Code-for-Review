class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """最长重复子数组
        1. dp
        dp[i][j]表示nums1以i结尾的子数组, 与nums2以j结尾的子数组的最长重复子数组长度
        i.  nums1[i] = nums2[j]
        dp[i][j] = dp[i-1][j-1] + 1
        ii. nums1[i] != nums2[j]
        dp[i][j] = 0
        """
        m, n = len(nums1), len(nums2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = 0
                res = max(res, dp[i][j])
        return res