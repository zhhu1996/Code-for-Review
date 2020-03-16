class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [first, second] -> [second, first] 且second中每个元素都大于first中每个元素
        l, r = 0, len(nums)-1
        while l < r: # 目的是查找first中第一个元素
            mid = (l + r) // 2
            # mid 在first中
            if nums[mid] < nums[r]:
                r = mid
            else: # mid 在second中
                l = mid + 1
        return nums[l]