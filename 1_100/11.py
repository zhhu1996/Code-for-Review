class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 1. 暴力, 超时

        # 2. 对撞指针，每次处理较小的高度的指针端，因为如果保持较小高度的指针不变而减小较高指针，那么面积一定会变小
        # 基于这种贪心的思想，每次移动小的高度的指针，保证算法会寻找更大面积，相当于每次只需要搜索一半的空间
        # 证明: https://leetcode.cn/problems/container-with-most-water/solutions/11491/container-with-most-water-shuang-zhi-zhen-fa-yi-do/?orderBy=most_votes
        # 时间复杂度O(n), 空间复杂度O(1)
        n, l, r = len(height), 0, len(height) - 1
        maxValue = 0
        while l < r:
            temp = (r - l) * min(height[l], height[r])
            if temp > maxValue:
                maxValue = temp
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxValue