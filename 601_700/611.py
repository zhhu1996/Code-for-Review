class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """有效三角形的个数
        1. 二分, 时间复杂度O(n*nlogn)

        2. 双指针, 时间复杂度O(n*n)
        """
        # # 1. 遍历较短的两条边, 查找第一个大于等于两边之和的值
        # cnt, size = 0, len(nums)
        # nums.sort()
        # print(nums)
        # for i in range(size-2):
        #     if nums[i] == 0:
        #         continue
        #     for j in range(i+1, size-1):
        #         # 在[j+1, size-1]中查找满足条件的第三条边
        #         tsum = nums[i] + nums[j] 
        #         if tsum > nums[-1]: # 全部满足
        #             cnt += (size-j-1)
        #         else: # 二分查找第一个大于等于tsum的值
        #             left, right = j+1, size-1
        #             while left < right:
        #                 mid = (left + right) // 2
        #                 if nums[mid] < tsum: # 下一轮搜索区间是 [mid + 1, right]
        #                     left = mid+1
        #                 else:                # 下一轮搜索区间是 [left, mid]
        #                     right = mid
        #             cnt += (left-j-1)
        # return cnt

        
        # 2.
        cnt, n = 0, len(nums)
        nums.sort()
        for i in range(n-2):
            if nums[i] == 0:
                continue
            j, k = i+1, i+2
            while k < n and j < n:
                if nums[k] - nums[j] < nums[i]:
                    cnt += (k-j)
                    k += 1
                else:
                    j += 1
        return cnt