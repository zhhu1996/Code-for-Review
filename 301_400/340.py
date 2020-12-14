from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """至多包含 K 个不同字符的最长子串
        1. 暴力遍历所有子串，判断是否满足条件

        2. 滑动窗口
        用hash表存储窗口内的字符个数
        窗口移动： 当窗口内的唯一字符串个数 < k时， j++
        窗口收缩：>k时，i++

        3. 滑动窗口
        用hash表存储字符出现的索引
        窗口移动： 当窗口内的唯一字符串个数 < k时， j++
        窗口收缩：>k时，删除索引最小的字符，i=minIndex+1
        """
        # # 方法1
        # maxLen = 0
        # n = len(s)
        # for i in range(n):
        #     for j in range(i+k,n):
        #         temp = s[i:j]
        #         if len(set(temp)) <= k:
        #             maxLen = max(maxLen, len(temp))
        # return maxLen

        # # 方法2
        # table = defaultdict(int)
        # i, j = 0, 0
        # n = len(s)
        # maxLen = 0
        # while j < n:
        #     table[s[j]] += 1
        #     while len(table.keys()) > k:
        #         table[s[i]] -= 1
        #         if table[s[i]] == 0:
        #             del table[s[i]]
        #         i += 1
        #     maxLen = max(maxLen, j - i + 1)
        #     j += 1
        # return maxLen

        # 方法3
        table = {}
        i, j = 0, 0
        n = len(s)
        maxLen = 0
        while j < n:
            table[s[j]] = j
            while len(table.keys()) > k:
                minIndex = min(table.values())
                del table[s[minIndex]]
                i = minIndex + 1
            maxLen = max(maxLen, j - i + 1)
            j += 1
        return maxLen
