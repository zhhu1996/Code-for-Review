class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """最长连续序列
        1. 暴力法：对nums先进行排序，然后寻找最长的连续序列，时间复杂度O(nlogn)
        2. 对于每个元素x，判断x+1,x+2,x+3...x+y是否在集合中，以此得到以元素x开始的最长序列；但是这样会做重复的计算，因为如果x-1也在集合中，
        那么必定比以x开始的序列要长，所以可将这一部分判断进行剪枝；时间复杂度O(n)
        """
        if not nums:
            return 0

        mset = set(nums)
        maxLen = 0
        for x in mset:
            if x - 1 not in mset: # x-1在set中则进行剪枝
                currentNum = x
                currentLen = 1
                while currentNum + 1 in mset:
                    currentNum += 1
                    currentLen += 1
                maxLen = max(maxLen, currentLen)
        return maxLen
