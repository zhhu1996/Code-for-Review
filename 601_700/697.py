class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 1. 统计最大频数后，根据最大频数算距离，有多个最大频数的情况下，注意比较
        # 2. 对于每个元素，计算左边界和右边界，同时统计每个元素出现的频数，注意有多个最大频数的话，注意比较
        table = {}
        maxnum, maxcnt = -1, 0
        for x in nums:
            if x not in table:
                table[x] = 1
            else:
                table[x] += 1
            if table[x] > maxcnt:
                maxcnt = table[x]
                maxnum = x
        result = []
        for k, v in table.items():
            if v == maxcnt:
                result.append(k)
        mincnt = float("inf")
        for r in result:
            left = nums.index(r)
            right = len(nums) - 1
            while right > left:
                if nums[right] == r:
                    break
                right -= 1
            if right - left + 1 < mincnt:
                mincnt = right - left + 1
        return mincnt

