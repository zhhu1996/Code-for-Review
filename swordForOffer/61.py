class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        """扑克牌中的顺子
        首先排序，计算0的个数，然后计算间隔的数字，如果0的个数 >= 间隔数，则满足
        如果出现相等数字，则直接返回不满足
        """

        nums.sort()
        i = 0
        zeroCnt = 0
        while i < len(nums):
            if nums[i] == 0:
                zeroCnt += 1
            else:
                break
            i += 1
        gapCnt = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                return False
            gapCnt += (nums[i+1] - nums[i] - 1)
            i += 1
        return gapCnt <= zeroCnt