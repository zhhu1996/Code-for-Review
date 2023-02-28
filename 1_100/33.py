class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """搜索旋转排序数组
        1. 第一次二分找到旋转位置, 根据位置判断目标值在哪一侧后再搜索一次
        2. 一次二分搜索
        """
        ## 1.
        # l, r = 0, len(nums)-1
        # while l <= r:
        #     mid = (l + r) // 2
        #     # f(l-1)>nums[-1], f(r+1)<=nums[-1]
        #     if nums[mid] <= nums[-1]:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # index =  l if l < len(nums) else 0
        # if target > nums[-1]:
        #     l, r = 0, index-1
        # else:
        #     l, r = index, len(nums)-1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return -1

        # 2.
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[-1]: # 右半段
                # [mid, r]有序
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # 左半段
                # [l, mid]有序
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1