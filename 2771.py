class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        """构造最长非递减子数组
        1. dp, 时间复杂度O(n)
        带维度单串, 位置i可不取, O(1)个子问题
        """
        n = len(nums1)
        dp = [[1,1] for _ in range(n)]
        ans = 1
        for i in range(1, n):
            # 选nums1
            if nums1[i] >= nums1[i-1]:
                dp[i][0] = max(dp[i][0], dp[i-1][0]+1)
            if nums1[i] >= nums2[i-1]:
                dp[i][0] = max(dp[i][0], dp[i-1][1]+1)
            # 选nums2
            if nums2[i] >= nums1[i-1]:
                dp[i][1] = max(dp[i][1], dp[i-1][0]+1)
            if nums2[i] >= nums2[i-1]:
                dp[i][1] = max(dp[i][1], dp[i-1][1]+1)
            ans = max(ans, dp[i][0], dp[i][1])
        return ans