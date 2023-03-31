class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """长度最小的子数组
        1. 变长滑动窗口, 时间复杂度O(n)

        2. 二分 + 前缀和, 时间复杂度O(nlogn)
        枚举连续子数组的左端点, 判断是否满足区间和>=target; 遍历取最小的区间作为结果
        """
        # # 1. 滑动窗口
        # n = len(nums)
        # l, r = 0, 0
        # cur_sum = 0
        # max_l = float('inf')
        # while r < n:
        #     cur_sum += nums[r]
        #     while cur_sum >= target:
        #         max_l = min(max_l, r-l+1)
        #         cur_sum -= nums[l]
        #         l += 1
        #     r += 1
        # return max_l if max_l != float('inf') else 0


        # 2. 二分
        n = len(nums)
        presum = [0]*(n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]
        max_l = float('inf')
        for i in range(n):
            if presum[n]-presum[i] < target:
                break
            l, r = i, n-1
            # 首次>=target
            while l <= r:
                mid = (l + r) // 2
                if presum[mid+1] - presum[i] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            if l < n:
                max_l = min(max_l, l-i+1)
        return max_l if max_l != float('inf') else 0