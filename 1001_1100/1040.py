from collections import defaultdict


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        """移动石子直到连续 II
        1. 首先求最大值
        总共有n个石头，总位置为s[-1]-s[0]+1个，当前元素占据的位置为n个，因此第一步可移动的空缺位置为s[-1]-s[0]+1-n个
        maxLen = s[-1]-s[0]+1-n - min(s[1]-s[0]-1, s[-1]-s[-2]-1)
        2. 求最小值
        滑动窗口法
        窗口扩大：若s[i] + n - 1 >= s[j],  j++
        窗口缩小：i++
        注意有特殊情况 j == n-1的时候， 2，3，4，5，7这种需要翻转2次
        """
        if not stones:
            return 0
        i, j = 0, 0
        n = len(stones)
        stones.sort()
        maxLen = stones[-1] - stones[0] + 1 - n - min(stones[1] - stones[0] - 1, stones[-1] - stones[-2] - 1)
        minLen = maxLen
        while i < n and j < n:
            while stones[i] + n - 1 < stones[j]:
                i += 1
            already = j - i + 1
            if already == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                minLen = min(minLen, 2)
            else:
                minLen = min(minLen, n - already)
            j += 1
        return [minLen, maxLen]
