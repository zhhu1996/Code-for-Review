class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """可被3整除的最大和
        1. 贪心: 取k个
        a, b, c分别表示mod1的集合,mod2的集合,mod3的集合
        a必定全选, b取x个, c取y个 => (x+2y)%3=0 => (x-y)%3=0 => x%3=y%3 

        2. 贪心: 丢k个
        a, b, c分别表示mod1的集合,mod2的集合,mod3的集合, t表示所有的和
        根据t%3的结果分情况讨论

        3. dp
        带维度单串, 位置i可不取, O(1)个子问题
        dp[i][j]表示前i个元素中最大的mod 3 = j的和
        dp[i][j] = max(dp[i-1][j], dp[i-1][(j-nums[i]%3)%3]+nums[i])
        """
        # # 1.
        # a = [x for x in nums if x % 3 == 0]
        # b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        # c = sorted([x for x in nums if x % 3 == 2], reverse=True)
        # suma = sum(a)
        # lb, lc = len(b), len(c)
        # ans = 0
        # for i in [lb-2, lb-1, lb]:
        #     if i < 0: continue
        #     for j in [lc-2, lc-1, lc]:
        #         if j >= 0 and i%3 == j%3:
        #             ans = max(ans, sum(a)+sum(b[:i])+sum(c[:j]))
        # return ans


        # # 2.
        # a = [x for x in nums if x % 3 == 0]
        # b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        # c = sorted([x for x in nums if x % 3 == 2], reverse=True)
        # t = sum(nums)
        # ans = 0
        # if t % 3 == 0:
        #     ans = t
        # elif t % 3 == 1:
        #     if len(b) >= 1:
        #         ans = max(ans, t-b[-1])
        #     if len(c) >= 2:
        #         ans = max(ans, t-c[-2]-c[-1])
        # else:
        #     if len(b) >= 2:
        #         ans = max(ans, t-b[-1]-b[-2])
        #     if len(c) >= 1:
        #         ans = max(ans, t-c[-1])
        # return ans


        # 3.
        n = len(nums)
        dp = [[0,0,0] for _ in range(n+1)]
        dp[0][0], dp[0][1], dp[0][2] = 0, -float('inf'), -float('inf')
        for i in range(1, 1+n):
            num = nums[i-1]
            for j in range(3):
                dp[i][(j+num%3)%3] = max(dp[i-1][(j+num%3)%3], dp[i-1][j]+num)
        return dp[n][0]