class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """环形子数组的最大和
        1. 暴力dp, 时间复杂度O(n^2)
        [3,-2,2,-3] =>
            [3,-2,2,-3]: maxdp1
            [-2,2,-3,3]: maxdp2
            [2,-3,3,-2]: maxdp3
            [-3,3,-2,2]: maxdp4
            => max(maxdpi) 

        2. 分情况讨论, 时间复杂度O(n)
        dp[i]表示以i结尾的子数组的最大和
        dp[i]的求解需要分情况讨论:
        i. 单区间, a[j:i], 0<=j<i
        即求a[:i]的子数组最大和
        ii. 双区间, a[0:i] | a[i+2:]
        令R[j] = a[j] + a[j+1] + ... + a[-1]
        则dp[i] = a[0] + a[1] + ... + a[i] + max(R[j]), j >= i+2
        """
        # # 1. 暴力dp
        # maxdp, n = -float('inf'), len(nums)
        # for i in range(n):
        #     maxdp_ = [-float('inf')] * n
        #     for j in range(n):
        #         index = (j + i) % n  
        #         maxdp_[j] = max(maxdp_[j-1]+nums[index], nums[index])
        #     maxdp = max(max(maxdp_), maxdp)
        # return maxdp

        # 2. 分情况讨论
        if not nums:
            return 0
        # 单区间
        dp1 = [x for x in nums]
        n = len(nums)
        for i in range(1, n):
            dp1[i] = max(dp1[i-1]+nums[i], nums[i])
        # 双区间
        r_sum = [x for x in nums]
        for i in range(n-2, -1, -1):
            r_sum[i] += r_sum[i+1]
        max_r = [-float('inf')]*n
        max_r[-1] = r_sum[-1]
        for i in range(n-2, -1, -1):
            max_r[i] = max(max_r[i+1], r_sum[i])
        cur = 0
        dp2 = [-float('inf')] * n
        for i in range(n):
            cur += nums[i]
            if i+2 < n:
                dp2[i] = max(cur, cur+max_r[i+2])
            else:
                dp2[i] = cur
        # maxdp
        maxdp = -float('inf')
        for i in range(n):
            maxdp = max(maxdp, dp1[i], dp2[i])
        return maxdp

