class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        """有序转化数组
        1. 双指针
        i.  a>0 => 最小值
        每次比较左端点l、右端点r, 大的选作当前步骤的最大值h, 而(l,r)的点<h
        ii. a<0 => 最大值
        每次比较左端点l、右端点r, 小的选作当前步骤的最小值h, 而(l,r)的点>h
        """
        res = [0]*len(nums)
        l, r = 0, len(nums)-1
        if a > 0:
            index = len(nums)-1
            while l <= r:
                lx, rx = nums[l], nums[r]
                lh = a*lx*lx + b*lx + c
                rh = a*rx*rx + b*rx + c
                if lh >= rh:
                    res[index] = lh 
                    l += 1
                else:
                    res[index] = rh
                    r -= 1
                index -= 1
        elif a < 0:
            index = 0
            while l <= r:
                lx, rx = nums[l], nums[r]
                lh = a*lx*lx + b*lx + c
                rh = a*rx*rx + b*rx + c
                if lh <= rh:
                    res[index] = lh 
                    l += 1
                else:
                    res[index] = rh
                    r -= 1
                index += 1  
        else:
            if b >= 0:
                for i in range(len(nums)):
                    res[i] = b*nums[i] + c
            else:
                for i in range(len(nums)):
                    res[len(nums)-1-i] = b*nums[i] + c
        return res