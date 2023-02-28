class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """寻找数组的中心下标
        1. 前缀和+后缀和

        2. 前缀和=后缀和
        => total-nums[i] == s[i]*2
        """
        n = len(nums)
        res = float('inf')
        presum, postsum = [0]*(n+1), [0]*(n+1)
        for i in range(n):
            presum[i+1] = presum[i] + nums[i]
        for i in range(n-1,-1,-1):
            postsum[i] = postsum[i+1] + nums[i]
            if postsum[i+1] == presum[i]:
                res = min(res, i)
        if res > n:
            res = -1
        return res