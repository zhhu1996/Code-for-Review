class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        """长度为K的无重复字符子串
        1. 滑动窗口 + set表
        维护一个大小为K的窗口，并用set存储当前窗口内所有出现过的字符
        如果窗口大小>K或者set中的字符重复出现，i++
        """
        if not S or K > len(S):
            return 0
        n = len(S)
        i, j, count = 0, 0, 0
        windowSet = set()
        while j < n:
            while j - i + 1 > K or S[j] in windowSet:
                windowSet.remove(S[i])
                i += 1
            windowSet.add(S[j])
            if j - i + 1 == K:
                count += 1
            j += 1
        return count
