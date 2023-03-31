class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        """两球之间的磁力
        1. 排序 + 二分
        最小磁力的搜索空间为[1, 10^9], 存在点p, 当x<=p时可以分配球; 当x>p时不可以分配球
        分配方式即为函数f(x)
        """

        def is_valid(nums, x, m):
            cnt = 1
            j, i = 0, 1 # j表示上个小球的位置
            while i < len(nums):
                if nums[i] - nums[j] >= x:
                    cnt += 1
                    j = i
                i += 1
            return cnt >= m

        position.sort() 
        l, r = 1, position[-1]
        while l <= r:
            mid = (l + r) // 2
            if is_valid(position, mid, m):
                l = mid + 1
            else:
                r = mid - 1
        # f(l-1) = True
        return l-1