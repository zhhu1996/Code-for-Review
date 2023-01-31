class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
        1. dp+暴力遍历, 时间复杂度O(n^3), 超时
        dp[i]表示得到target[..i]的最小子序列数量
        dp[i] = max(dp[j-1]+1), 0<=j<i && target[j..i]是source的子序列
        
        2. dp+贪心, 时间复杂度O(n^2)
        贪心: 每一步尽可能合并字符串(证明: https://leetcode.cn/problems/shortest-way-to-form-string/solution/greedy-zheng-ming-by-xi-er-wen-dfrs/)
        dp: dp[i]表示得到target[..i]的最小子序列数量
            如果target[i]可以被合并到i-1结尾的子序列中, dp[i] = dp[i-1]
            否则 dp[i] = dp[i-1]+1      
        
        3. dp+贪心+二分, 时间复杂度O(nlogn)
        贪心: 每一步尽可能合并字符串
        dp: dp[i]表示得到target[..i]的最小子序列数量
            如果target[i]可以被合并到i-1结尾的子序列中, dp[i] = dp[i-1]
            否则 dp[i] = dp[i-1]+1
        二分: 判断target[i]是否能被合并到i-1结尾的子序列
            将source中的字符与位置存储到map中,target[i]在source中的位置 > target[i-1]在source中的位置即可
        """
        # 2.
        if not source or not target:
            return -1
        ss, st = set(source), set(target)
        for c in st:
            if c not in ss:
                return -1

        def is_subseq(a, b):
            left, right = 0, 0
            while left < len(a) and right < len(b):
                if a[left] == b[right]:
                    left += 1
                    right += 1
                else:
                    left += 1
            return right == len(b)
        
        n = len(target)
        dp = [float('inf')] * n
        dp[0] = 1
        cur = target[0]
        for i in range(1, n):
            cur += target[i]
            if is_subseq(source, cur):
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + 1
                cur = target[i]
        return dp[n-1]

        # # 3.
        # char_map = {}
        # for i in range(len(source)):
        #     if source[i] in char_map:
        #         char_map[source[i]].append(i)
        #     else:
        #         char_map[source[i]] = [i]
        # if target[0] not in char_map:
        #     return -1

        # def find_next(v, k):
        #     left, right = 0, len(v)-1
        #     while left < right:
        #         mid = (left + right) // 2
        #         if v[mid] <= k:
        #             left = mid + 1
        #         else:
        #             right = mid
        #     if v[left] > k:
        #         return v[left]
        #     else:
        #         return -1

        # dp = 1
        # ptr = char_map[target[0]][0]
        # for i in range(1, len(target)):
        #     if target[i] not in char_map:
        #         return -1
        #     ptr = find_next(char_map[target[i]], ptr)
        #     if ptr < 0:
        #         dp += 1
        #         ptr = char_map[target[i]][0]
        #     else:
        #         dp = dp

        # return dp
        