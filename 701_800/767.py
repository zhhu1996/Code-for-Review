class Solution:
    def reorganizeString(self, S: str) -> str:
        """
        统计每个字母出现的次数，
        奇数长度：x > len(S) // 2 + 1
        偶数长度：x > len(S) // 2
        """
        table = {}
        maxcnt = 0
        maxc = ""
        for c in S:
            if c not in table:
                table[c] = 1
            else:
                table[c] += 1
            if maxcnt < table[c]:
                maxcnt = max(maxcnt, table[c])
                maxc = c
        lenS = len(S)
        if lenS % 2 == 0 and maxcnt > lenS // 2:
            return ""
        if lenS % 2 != 0 and maxcnt > lenS // 2 + 1:
            return ""
        A = []
        array = [0]*lenS
        for k, v in sorted(table.items(), key=lambda x: x[1], reverse=True):
            A.extend([k]*v)
        j = 0
        for i in range(lenS):
            array[j] = A[i]
            j += 2
            if j >= lenS:
                j = 1
        return "".join(array)