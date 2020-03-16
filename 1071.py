class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 1. 暴力法
        if len(str1) < len(str2):
            mins, maxs = str1, str2
        else:
            mins, maxs = str2, str1

        def isgcd(s1, s2):
            len1, len2 = len(s1), len(s2)
            if s1 == s2[:len1] and s1 * (len2 // len1) == s2:
                return True
            else:
                return False

        for i in range(len(str2)):  # 贪心
            if isgcd(str2[i:], str2) and isgcd(str2[i:], str1):
                return str2[i:]

        return ""
