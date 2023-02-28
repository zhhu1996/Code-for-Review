class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """删除子数组的最大得分
        1. 变长滑动窗口
        set / hash表记录窗口内的字符
        """
        # 1. set
        n, l, r = len(nums), 0, 0
        res, cur = 0, 0
        pos = set() # 存储窗口内已经出现过的字符
        while r < n:
            if nums[r] not in pos:
                cur += nums[r]
                pos.add(nums[r])
                if cur > res:
                    res = cur 
            else: # 出现重复元素
                while nums[l] != nums[r]:
                    cur = cur - nums[l]
                    pos.remove(nums[l])
                    l += 1
                l += 1
            r += 1
        return res

        # 2. hash表
        # n, l, r = len(nums), 0, 0
        # res, cur = 0, 0
        # pos = {}
        # while r < n:
        #     if nums[r] not in pos:
        #         cur += nums[r]
        #         pos[nums[r]] = r 
        #         if cur > res:
        #             res = cur 
        #     else: # 出现重复元素
        #         while l < pos[nums[r]]:
        #             cur = cur - nums[l]
        #             del pos[nums[l]]
        #             l += 1
        #         cur = cur - nums[l] + nums[r]
        #         pos[nums[r]] = r
        #         l += 1
        #     r += 1
        # return res