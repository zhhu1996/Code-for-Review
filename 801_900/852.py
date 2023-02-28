class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """山脉数组的峰顶索引
        1. 设封顶索引为j, 根据定义有
        对于i < j => arr[i] > arr[i-1]
        对于i > j => arr[i] < arr[i-1]
        """
        # # 1. 全闭区间[left, right] 
        # left, right = 1, len(arr)-2
        # while left <= right:
        #     # 循环不变量
        #     # nums[left-1] 满足 arr[mid] > arr[mid-1]
        #     # nums[right+1]满足 arr[mid] < arr[mid-1]
        #     mid = (left + right) // 2
        #     if arr[mid] > arr[mid-1]:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return left-1

        # 2. 左闭右开区间[left, right)
        left, right = 1, len(arr)-1
        while left < right:
            # 循环不变量
            # nums[left-1] 满足 arr[mid] > arr[mid-1]
            # nums[right]  满足 arr[mid] < arr[mid-1]
            mid = (left + right) // 2
            if arr[mid] > arr[mid-1]:
                left = mid + 1
            else:
                right = mid
        return left-1

        # # 3. 全开区间(left, right)
        # left, right = 0, len(arr)-1
        # while left + 1 < right:
        #     # 循环不变量
        #     # num[left]  满足 arr[mid] > arr[mid-1]
        #     # num[right] 满足 arr[mid] < arr[mid-1]
        #     mid = (left + right) // 2
        #     if arr[mid] > arr[mid-1]:
        #         left = mid
        #     else:
        #         right = mid
        # return left
