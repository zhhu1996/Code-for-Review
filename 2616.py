class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """最小化数对的最大差值
        1. 二分 + 贪心, 时间复杂度O(nlogn)
        最小化最大差值 -> 二分, check函数: 在最大差值限制下可以取的最多对数
        贪心: 为取最多对, 每一对的元素必相邻, 且越早匹配越好
        """
        nums.sort()

        def check(x):
            cnt, i = 0, 0
            while i < len(nums)-1:
                if nums[i+1] - nums[i] <= x:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p

        l, r = 0, nums[-1]-nums[0]
        while l <= r:
            mid = (l + r) // 2
            if not check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l