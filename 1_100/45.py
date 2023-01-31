class Solution:
    def jump(self, nums: List[int]) -> int:
        # # 1. 动态规划, 时间O(n^2)
        # # => dp[i] = min(dp[j]+1, dp[i]) if j+nums[j] >= i, 0<=j<=i-1
        # dp = [float('inf')]*len(nums)
        # dp[0] = 0
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if j + nums[j] >= i:
        #             dp[i] = min(dp[i], dp[j]+1)
        # return dp[-1]

        # # 2. 贪心+双指针, pos表示最远可达位置, cnt为最小跳跃次数, 等于pos更新的次数
        # pos, cnt, i = 0, 0, 0
        # while i < len(nums):
        #     if pos >= len(nums)-1:
        #         break
        #     target = 0
        #     for j in range(i, pos+1):
        #         target = max(target, j+nums[j])
        #     if target > pos:
        #         cnt += 1
        #         i = pos + 1
        #         pos = target
        #     else:
        #         return -1
        # return cnt 

        # 3. 更简洁的贪心+双指针
        pos, lpos, cnt = 0, 0, 0
        for i in range(len(nums)-1):
            if i <= pos:
                pos = max(pos, i+nums[i])
                if i == lpos:
                    cnt += 1
                    lpos = pos
        return cnt
        