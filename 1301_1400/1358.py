class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """包含所有三种字符的子字符串数目
        1. 滑动窗口端点计数
        [l..r]是包含三种字符的最小字符串 => [l..r,r+1..n-1]都满足条件 => n-r个字符串
        遍历数组, 维护符合条件的窗口即可

        2. 转化成滑动窗口求解区间计数
        """
        from collections import defaultdict
        l, r, res, n = 0, 0, 0, len(s)
        w_map = defaultdict(int)
        matchs = 0
        while r < n:
            w_map[s[r]] += 1
            if w_map[s[r]] == 1:
                matchs += 1
            while matchs >= 3:
                res += n-r
                w_map[s[l]] -= 1
                if w_map[s[l]] == 0:
                    matchs -= 1
                l += 1
            r += 1
        return res