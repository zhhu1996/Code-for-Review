class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        """
        1. 暴力法：寻找[minSize, maxSize]之间的所有子串，并统计每个子串出现的次数，时间复杂度
        2. 其实maxSize的限定并没有用，题干中要求子串的唯一字符数<=maxLetters并且出现次数最多，对于maxSize长的子串，倘若满足条件，那么
        minSize长的子串也一定满足条件，因此出现次数最多的子串必定从minSize的子串中进行挑选。
        """
        # n = len(s)
        # table = {}
        # maxcnt = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         if j - i + 1 < minSize or j - i + 1 > maxSize:
        #             continue
        #         cur = s[i: j + 1]
        #         if len(set(cur)) > maxLetters:
        #             break
        #         else:
        #             if cur in table:
        #                 table[cur] += 1
        #             else:
        #                 table[cur] = 1
        #             maxcnt = max(maxcnt, table[cur])
        # return maxcnt

        n = len(s)
        table = {}
        maxcnt = 0
        for i in range(n-minSize+1):
            j = i + minSize
            cur = s[i: j]
            if len(set(cur)) > maxLetters:
                continue
            else:
                if cur in table:
                    table[cur] += 1
                else:
                    table[cur] = 1
                maxcnt = max(maxcnt, table[cur])
        return maxcnt





