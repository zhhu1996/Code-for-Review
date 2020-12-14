from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """至多包含两个不同字符的最长子串
        1. 滑动窗口法
        用双指针维护一个窗口，hash表记录窗口内的字符出现的次数
        """
        counter = defaultdict(int)
        n = len(s)
        left = 0
        maxLen = 0
        for right in range(n):
            counter[s[right]] += 1
            if len(counter) > 2:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            else:
                maxLen = max(maxLen, right - left + 1)
        return maxLen

