class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # # 1. 回溯求所有组合:C(n, k), 然后判断, 超时
        # self.res = 0
        
        # def gen_comb(nums, cur, index):
        #     if len(cur) == 3:
        #         x,y,z = cur[0], cur[1], cur[2]
        #         if x+y > z and x+z > y and y+z > x:
        #             self.res += 1
        #         return 
        #     for i in range(index, len(nums)):
        #         cur.append(nums[i])
        #         gen_comb(nums, cur, i+1)
        #         cur.pop()

        # gen_comb(nums, [], 0)
        # return self.res    

        # 2. 遍历较短的两条边, 查找第一个大于等于两边之和的值
        cnt, size = 0, len(nums)
        nums.sort()
        print(nums)
        for i in range(size-2):
            if nums[i] == 0:
                continue
            for j in range(i+1, size-1):
                # 在[j+1, size-1]中查找满足条件的第三条边
                tsum = nums[i] + nums[j] 
                if tsum > nums[-1]: # 全部满足
                    cnt += (size-j-1)
                else: # 二分查找第一个大于等于tsum的值
                    left, right = j+1, size-1
                    while left < right:
                        mid = (left + right) // 2
                        if nums[mid] < tsum: # 下一轮搜索区间是 [mid + 1, right]
                            left = mid+1
                        else:                # 下一轮搜索区间是 [left, mid]
                            right = mid
                    cnt += (left-j-1)
        return cnt