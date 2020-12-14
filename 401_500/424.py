from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """替换后的最长重复子串
        1. 滑动窗口 + hash表
        用双指针i，j维护一个滑动窗口，hash表记录窗口内各个字符的个数
        满足可替换的最长重复子串的条件是：
        如果s[j]是字典中的最大值，那么
        max(dict[v])+ k >= j - i
        否则
        max(dict[v])+ 1 + k >= j - i + 1
        不满足的时候，调整i指针

        2. 简化版
        窗口扩张：i不变，j++
        窗口滑动：i++，j++
        """
        # counter = defaultdict(int)
        # maxLen = 0
        # i, j = 0, 0
        # while i < len(s) and j < len(s):
        #     maxCount = 0
        #     for key, value in counter.items():
        #         maxCount = max(maxCount, value)
        #     if counter[s[j]] == maxCount:
        #         T = maxCount + 1
        #     else:
        #         T = maxCount
        #     if T + k >= j - i + 1:
        #         counter[s[j]] += 1
        #         maxLen = max(maxLen, j - i + 1)
        #         j += 1
        #     else:
        #         counter[s[i]] -= 1
        #         i += 1
        # return maxLen

        counter = defaultdict(int)
        maxLen, maxCount = 0, 0
        i = 0
        for j in range(len(s)):
            counter[s[j]] += 1
            maxCount = max(maxCount, counter[s[j]])
            if maxCount + k >= j - i + 1:
                maxLen = max(maxLen, j-i+1)
            else:
                if counter[s[i]] == maxCount:
                    maxCount -= 1
                counter[s[i]] -= 1
                i += 1
        return maxLen




