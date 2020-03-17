class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [first, second] -> [second, first] 且second中每个元素都大于first中每个元素

        1. left < mid && mid < right: 没有旋转，最小值在[left, mid]之间
        2. left < mid && mid > right: 有旋转，最小值在[mid+1, right]之间
        3. left > mid && mid > right: 不可能情况
        4. left > mid && mid < right: 有旋转，最小值在[left, mid]之间

        比较4种情况，1/4都对应mid < right，2对应mid > right
        """
        l, r = 0, len(nums)-1
        while l < r: # 目的是查找first中第一个元素
            mid = (l + r) // 2
            # mid 在first中
            if nums[mid] < nums[r]:
                r = mid
            else: # mid 在second中
                l = mid + 1
        return nums[l]