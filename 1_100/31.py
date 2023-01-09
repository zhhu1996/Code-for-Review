class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # 1. 暴力解法: 从右向左查找第一个顺序对, 交换顺序后, 升序排列后面的数组, 时间O(n^2)
        # for i in range(len(nums)-1, -1, -1):
        #     for j in range(len(nums)-1, i, -1):
        #         if nums[j] > nums[i]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             nums[i+1:] = sorted(nums[i+1:])
        #             return
        # nums.sort()

        # 2. 解法1的优化, 时间O(n)
        # => 根据降序数组的长度, 先找到需要调整的左边界j
        j = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                j = i - 1
                break
        if j == -1:
            nums.sort()
            return

        # 交换元素后需要排序
        for i in range(len(nums) - 1, j, -1):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                # 可以不使用排序，直接反转就行，因为仍然满足顺序, nums[j+1:] = nums[-1:j:-1]
                nums[j + 1:] = sorted(nums[j + 1:])
                break

