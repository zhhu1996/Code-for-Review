class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i]表示nums[:i]可取得的最大收益
        分两种情况: 
        i.  首取尾不取
            相当于丢弃最后一个元素的打家劫舍I
        ii. 尾取首不取
            dp[0]限定为0
        状态转移方程均为
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        n = len(nums)
        dp1 = [0] * (n-1)
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
        dp2 = [0] * n
        dp2[1], dp2[2] = nums[1], max(nums[1], nums[2])
        for i in range(3, n):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])
        return max(dp1[n-2], dp2[n-1])