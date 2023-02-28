class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """最长定差子序列
        1. dp + 哈希表(加速)
        单串, 位置i必须取, 依赖O(1)个子问题
        dp[i]: 以arr[i]结尾的最长定差子序列
            dp[i] = max(dp[j] + 1) if arr[i]-arr[j] = d
        哈希表: 存储arr[i]最近一次出现的位置
        """
        n = len(arr)
        if n == 0: return 0
        dp = [1]*n
        arr_map = defaultdict(int)
        arr_map[arr[0]] = 0
        for i in range(1, n):
            j = arr[i] - difference
            if j in arr_map:
                dp[i] = max(dp[i], dp[arr_map[j]]+1)
            arr_map[arr[i]] = i
        return max(dp)