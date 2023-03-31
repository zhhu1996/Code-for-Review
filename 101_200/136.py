class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """只出现一次的数字
        1. 异或运算, 时间复杂度O(n), 空间复杂度O(1)
        """
        res = 0
        for num in nums:
            res = res ^ num
        return res