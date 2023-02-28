class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #         # 1. 暴力解，直接遍历所有情况，找出最大值，时间复杂度O(n^3)
        #         if not s:
        #             return 0
        #         maxCnt, thisCnt = 1, 1
        #         for i in range(len(s)-1):
        #             thisCnt = 1
        #             for j in range(i+1, len(s)):
        #                 if s[j] in s[i:j]:
        #                     break
        #                 else:
        #                     thisCnt += 1
        #             if thisCnt > maxCnt:
        #                 maxCnt = thisCnt

        #         return maxCnt

        ## 2. 滑动窗口法，用set维护[i, j]的元素，用更低的时间复杂度实现查询，时间复杂度O(2*n)，n是字符串最大长度
        # n, l, r = len(s), 0, 0
        # exists = set()
        # res = 0
        # while r < n:
        #     if s[r] not in exists:
        #         exists.add(s[r])
        #         if res < r-l+1:
        #             res = r-l+1
        #     else:
        #         while s[l] != s[r]:
        #             exists.remove(s[l])
        #             l += 1
        #         l += 1
        #     r += 1
        # return res

        # 3. 优化版本的滑动窗口法，除了维护每个元素是否出现，还保存元素出现的位置，这样在s[j] in set[i, j-1]的时候，跳过出现的位置
        data = {}
        i, j, n = 0, 0, len(s)
        res = 0
        while j < n:
            if s[j] in data:  # 加速部分
                i = max(data[s[j]] + 1, i)
            data[s[j]] = j
            j += 1
            res = max(j - i, res)

        return res