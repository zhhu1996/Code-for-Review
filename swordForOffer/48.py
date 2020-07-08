class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """最长不含重复字符的子字符串
        1. 动态规划: f[i]表示以i结尾的不重复子字符串的最大长度
        if s[i] not in s[:i]:  f[i] = f[i-1] + 1
        if s[i] in s[:i]:
            d = i - s[i]上次出现的位置
            if d < f[i-1]:
                f[i] = d
            else:
                f[i] = f[i-1] + 1
        """
        if not s:
            return 0
        position = {}
        f = []
        for i in range(len(s)):
            if s[i] not in position:
                if i == 0:
                    f.append(1)
                else:
                    f.append(f[i-1]+1)
            else:
                d = i - position[s[i]]
                if d <= f[i-1]:
                    f.append(d)
                else:
                    f.append(f[i-1]+1)
            position[s[i]] = i
        return max(f)