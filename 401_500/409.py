class Solution:
    def longestPalindrome(self, s: str) -> int:
        """最长回文串
        1. 贪心
        每次取成对的字符构建回文串, 最后再搭配个单字符
        """
        from collections import defaultdict

        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        ans = 0
        flag = True
        for k, v in counter.items():
            if v % 2 == 0:
                ans += v
            else:
                if flag:
                    ans += v
                    flag = False
                else:
                    ans += v // 2 * 2
        return ans