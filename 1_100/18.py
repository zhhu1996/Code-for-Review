class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 类似3数之和，再加一个循环。注意不能提前剪枝
        if not nums or len(nums) < 4:
            return []

        res = []
        nums.sort()
        for i in range(len(nums)-3):#[-4,-1,-1,0,1,2]
            for j in range(i+1, len(nums)-2):
                if (i > 0 and nums[i] == nums[i-1]) or (j > i+1 and nums[j] == nums[j-1]): # 去重
                    continue
                p, k = j+1, len(nums)-1
                while p < k:
                    if nums[i] + nums[j] + nums[p] + nums[k] == target:
                        res.append([nums[i], nums[j], nums[p], nums[k]])
                        # 去重
                        while p < k and nums[p] == nums[p+1]:
                            p += 1
                        while p < k and nums[k] == nums[k-1]:
                            k -= 1
                        p += 1
                        k -= 1
                    elif nums[i] + nums[j] + nums[p] + nums[k] > target:
                        k -= 1
                    else:
                        p += 1

        return res