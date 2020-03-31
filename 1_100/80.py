class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 双指针， 只要num[i] != nums[j-1]即表示是正确的
        if not nums:
            return 0

        if len(nums) <= 2:
            return len(nums)

        i, j = 2, 1
        cnt = 2
        while i < len(nums):
            if nums[i] != nums[j - 1]:
                j += 1
                nums[j] = nums[i]
                cnt += 1
            i += 1

        return cnt