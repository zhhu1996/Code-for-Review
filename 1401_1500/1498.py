class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """满足条件的子序列数目
        首先只要求满足条件的子序列，可以对数组排序之后使用双指针求解；
        left,right=0,n-1
        当前满足条件的窗口内包含的子序列个数为
        2**(right-left)个
        分为nums[left] + 右边right-left个元素排列组合
        """

        nums.sort()
        if nums[0] * 2 > target:
            return 0

        left = 0
        right = len(nums) - 1
        res = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                res += 2 ** (right - left)
                left += 1
            else:
                right -= 1
        return res % (10 ** 9 + 7)
