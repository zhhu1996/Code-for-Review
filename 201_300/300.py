class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        1. 动态规划: dp[i]表示以i结尾的最长子序列的长度
        => dp[i] = max(dp[j]+1), j < i and a[i]>a[j]
        """
        # if not nums:
        #     return 0
        # dp = [1]
        # for i in range(1, len(nums)):
        #     result = 1
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             result = max(dp[j]+1, result)
        #     dp.append(result)
        # return max(dp)

        """
        2. 贪心+二分查找: https://leetcode.cn/problems/longest-increasing-subsequence/solutions/7196/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
        => tail[i]表示长度为i+1的所有最长上升子序列的结尾的最小值, tail也是一个严格上升数组
        遍历nums:
        step1: 如果nums数组的当前元素严格大于tail的尾元素, 就添加到tail数组的末尾
        step2: 在有序数组tail中查找第一个大于num的元素, 更新为num
        """
        if len(nums) <= 1:
            return len(nums)
        tail = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue
            left, right = 0, len(tail)-1
            while left < right:
                mid = (left + right) // 2
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = nums[i]
        return len(tail)