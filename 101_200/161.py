class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """相距为1的编辑距离
        1.
        两字符串的长度相差必须小于2
        i.长度相等的情况下：
            s[i] != t[i], 那么s[i+1:]必须等于t[i+1:]
        ii.长度相差1的情况，假设len(s)+1==len(t)
            s[i] != t[i], 那么s[i:]必须等于t[i+1:]

        """
        if len(s) > len(t):
            s, t = t, s
        if len(t) - len(s) > 1:
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]
        # 如果s中的字符全部匹配的话，只需要判断是否t比s多一个字符即可
        return len(t) - len(s) == 1

        # if len(s) > len(t):
        #     s, t = t, s
        # i, j = 0,0
        # cnt = 0
        # if len(s) == len(t):
        #     for i in range(len(s)):
        #         if s[i] != t[i]:
        #             cnt += 1
        # else:
        #     while i < len(s) and j < len(t):
        #         if s[i] == t[j]:
        #             i += 1
        #             j += 1
        #         else:
        #             j += 1
        #             cnt += 1
        #     if j < len(t):
        #         cnt += len(t) - j

        # return cnt == 1