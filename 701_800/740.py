class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """删除并获得点数
        1. dp + 哈希表
        单串, 位置i可不取, O(1)子问题
        dp[i]: 到数字i时的最大收益
        """
        from collections import defaultdict
        counter = defaultdict(int)
        max_num = 0
        for num in nums:
            counter[num] += 1
            max_num = max(max_num, num)
        dp = [0] * (max_num+1)
        for i in range(1, max_num+1):
            if i in counter:
                dp[i] = max(dp[i-1], dp[i-2]+i*counter[i])
            else:
                dp[i] = dp[i-1]
        return dp[max_num]
            