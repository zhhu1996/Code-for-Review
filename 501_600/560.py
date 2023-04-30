class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """和为k的子数组
        1. 前缀和, 时间复杂度O(n), 空间复杂度O(n)
        用字典存储前缀和, key为前缀和s[i], value为出现次数
        更新前缀和时, 若s[i]-k已存在字典中, 说明找到一组连续区间满足要求
        """
        n = len(nums)
        dp = [0 for i in range(1+n)]
        cnt_m = {0: 1} # dp[i+1]==k
        res = 0
        for i in range(n):
            dp[i+1] = nums[i] + dp[i]
            if dp[i+1] - k in cnt_m:
                res += cnt_m[dp[i+1]-k]
            if dp[i+1] in cnt_m:
                cnt_m[dp[i+1]] += 1
            else:
                cnt_m[dp[i+1]] = 1
        return res