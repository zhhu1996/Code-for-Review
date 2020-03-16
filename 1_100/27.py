class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 1. 调用库函数删除，时间复杂度O(n^2)

        # 2. 维护一个非val值的序列，并用指针指向其最后一个元素，迭代原数组如果不是val则加入序列，否则进行下一轮迭代，
        # 时间复杂度O(n)
        if not nums:
            return 0
        i, j, n = -1, 0, len(nums)
        while j < n:
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
            j += 1

        return i + 1