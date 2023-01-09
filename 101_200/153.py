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

        """
        例 3：[7, 8, 9, 10, 11, 12, 1, 2, 3]

        “中间数” 11 比右边界 3 大，因此中间数左面的数（包括中间数）都不是“旋转排序数组”的最小值，可以把下一轮搜索的左边界设置成中间数位置 + 1，即 left = mid + 1。

        例 4：[7, 8, 1, 2, 3]

        “中间数” 1 比右边界 3 小，说明，中间数到右边界是递增的，那么中间数右边的（不包括中间数）一定不是“旋转排序数组”的最小值，可以把它们排除，不过中间数有可能是目标数，就如本例，因此，在下一轮搜索把右边界设置为 right = mid。

        从例 3 和例 4 可以看出，不论中间数比右边界大，还是中间数比右边界小，我们都可以排除掉将近一半的元素，把原始问题转换成一个规模更小的子问题，这正是“减而治之”思想的体现，因此思路 2 可行。
        """
        # left, right = 0, len(nums)-1
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] > nums[right]:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return nums[left]