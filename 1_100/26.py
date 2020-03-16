class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 1.用一个指针指向不重复序列的最后一个元素，遍历数组时每次将新的元素和唯一值序列的最后一个元素进行比较，如果相同则
        # 表示是重复元素，则进行下一轮迭代；如果不相同则将其加入唯一值序列
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
