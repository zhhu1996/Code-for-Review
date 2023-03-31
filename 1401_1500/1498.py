class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """满足条件的子序列数目
        1. 排序 + 二分, 时间复杂度O(nlogn)
        先排序, 然后枚举起点, 二分查找满足条件的右端点

        2. 双指针, 时间复杂度O(n)
        双指针相向移动, 统计满足条件的组合
        """
        # # 1.
        # n = len(nums)
        # nums.sort()
        # res = 0
        # for i in range(n):
        #     k = target - nums[i]
        #     l, r = i, n-1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if nums[mid] <= k:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     # f(l-1)<=k, f(l)>k
        #     if l-1 >= i:
        #         # res += 2**(l-i-1)-1
        #         # res += pow(2, l-i-1)-1
        #         res += (1<<(l-i-1)) - 1
        #         if nums[i]*2 <= target:
        #             res += 1
        # return res % (10**9 + 7)


        # # 2.
        i, j, cnt = 0, len(nums)-1, 0
        nums.sort()
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else: # 统计以nums[i]为最小元素的子序列
                # cnt += 2**(j-i)-1
                cnt += (1<<(j-i)) - 1
                if nums[i] * 2 <= target:
                    cnt += 1
                i += 1
        return cnt % (10**9 + 7)