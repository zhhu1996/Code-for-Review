class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        """使字符串总不同字符的数目相等
        1. 暴力枚举
        一共26*26种组合, 时间复杂度O(256)
        """
        c1, c2 = Counter(word1), Counter(word2)
        for k1 in c1.keys():
            for k2 in c2.keys():
                l1, l2 = len(c1), len(c2)
                if k1 == k2:
                    if l1 == l2:
                        return True
                else:
                    if c1[k1] == 1:
                        l1 -= 1
                    if c1[k2] == 0:
                        l1 += 1
                    if c2[k2] == 1:
                        l2 -= 1
                    if c2[k1] == 0:
                        l2 += 1
                    if l1 == l2:
                        return True
        return False