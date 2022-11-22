class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """132模式
        1. 暴力，时间复杂度O(n^3)

        2. 对于1的优化，最差时间复杂度O(n^3)，最好时间复杂度O(n^2)

        3. 存在i<j<k，使得a[i]<a[k]<a[j]
        即寻找公共的顺序对(i,j),(i,k)，使得a[j]>a[k]
        """
        # # 方法1
        # if len(nums) < 3:
        #     return False
        #
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] < nums[k] and nums[k] < nums[j]:
        #                 return True
        # return False

        # 方法2
        if len(nums) < 3:
            return False

        for i in range(len(nums)-2):
            k = len(nums)-1
            while k > i:
                if nums[k] > nums[i]:
                    j = i + 1
                    while j < k:
                        if nums[j] > nums[k]:
                            return True
                        j += 1
                k -= 1
        return False
