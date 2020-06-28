class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def isMatchCore(s, p, index1, index2):
            if index1 >= len(s) and index2 >= len(p):
                return True
            if index2 >= len(p) and index1 < len(s):
                return False
            if index2 < len(p) - 1 and p[index2 + 1] == '*':  # 下一个元素是*
                if index1 < len(s) and (s[index1] == p[index2] or p[index2] == '.'):  # 当前元素匹配
                    # 1.匹配串+1, 模式串不动
                    # 2.忽略*: 匹配串不动，模式串+2
                    # 3.匹配串+1，模式串+2(被上述两种情况包含了)
                    return isMatchCore(s, p, index1 + 1, index2) \
                           or isMatchCore(s, p, index1, index2 + 2)
                else:  # 当前元素不匹配
                    return isMatchCore(s, p, index1, index2 + 2)
            if index1 < len(s) and (s[index1] == p[index2] or p[index2] == '.'):
                return isMatchCore(s, p, index1 + 1, index2 + 1)
            return False

        return isMatchCore(s, p, 0, 0)
