class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        """找两个和为目标值且不重叠的子数组
        1. 前缀和+后缀和, 并保存状态, 时间复杂度O(n^2), 超时
           分别根据前缀和、后缀和得到目标等于target的最小区间, 然后去组合这两个区间
        
        2. 单串dp, 时间复杂度O(n)
        dp[i]表示到位置i的和为target的最小子数组长度, 位置i可取可不取
        res = min(i - pre_map[presum-target] + dp[pre_map[presum-target]])
        """
        n = len(arr)
        presum, pre_map = 0, {0:0}
        dp = [float('inf')]*(1+n)
        res = float('inf')
        for i in range(1,1+n):
            presum += arr[i-1]
            if presum - target in pre_map: # 区间1已找到
                len1 = i - pre_map[presum-target]
                dp[i] = min(dp[i-1], len1)
                res = min(res, len1 + dp[pre_map[presum-target]])
            else:
                dp[i] = dp[i-1]
            # 存储前缀和的最近一次位置
            pre_map[presum] = i
        if res > n:
            res = -1
        return res