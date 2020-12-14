class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """最大连续1的个数
        1. 滑动窗口
        当前窗口不满足时，i = j+1

        """
        if not nums:
            return 0
        i, j = 0, 0
        n = len(nums)
        maxLen = 0
        while i < n and j < n:
            if nums[j] == 1:
                maxLen = max(maxLen, j - i + 1)
                j += 1
            else:
                i = j + 1
                j += 1
        return maxLen
