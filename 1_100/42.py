class Solution:
    def trap(self, height: List[int]) -> int:
        """接雨水
        1. 暴力搜索, 时间O(n^2)
        遍历所有的位置，计算当前位置能接的雨水量=min(当前位置左侧的最高峰，当前位置右侧的最高峰) - 当前位置的高度,最后求和;

        2. 动态规划求每个位置左边的最大值以及每个位置右边的最大值, 时间复杂度O(n)
        maxLeft[i]表示位置<=i的最大高度
        maxRight[i]表示位置>=i的最大高度

        3. 双指针法
        left, right指针分别指向height[0]与height[n-1]
        leftMax表示当前left指针左侧的最大高度, rightMax表示当前right指针右侧的最大高度
        可以确保的是h[left]<=leftMax, h[right]<=rightMax, 由于当前位置能接的雨水量与min(左侧最大值, 右侧最大值)相关,
        那么只要leftMax < rightMax, 那么left位置的面积就知道了, left++;
        只要leftmax > rightMax, 那么right位置的面积就知道了, right--

        """
        # # 方法1
        # result = 0
        # n = len(height)
        # for i in range(1, n-1):
        #     maxLeft, maxRight = 0, 0
        #     for j in range(i):
        #         if height[j] > height[i]:
        #             maxLeft = max(maxLeft, height[j])
        #     for j in range(i+1, n):
        #         if height[j] > height[i]:
        #             maxRight = max(maxRight, height[j])
        #     result += max(0, min(maxRight, maxLeft) - height[i])
        # return result

        # # 方法2
        # if not height:
        #     return 0
        # result = 0
        # n = len(height)
        # maxLeft = [0]*n
        # maxRight = [0]*n
        # maxLeft[0] = height[0]
        # for i in range(1,n):
        #     maxLeft[i] = max(maxLeft[i-1], height[i])
        # maxRight[-1] = height[-1]
        # for j in range(n-2,0,-1):
        #     maxRight[j] = max(maxRight[j+1], height[j])
        # for k in range(1,n):
        #     result += min(maxLeft[k], maxRight[k]) - height[k]
        # return result

        # 方法3
        result = 0
        n = len(height)
        left, right, leftMax, rightMax = 0, n-1, 0, 0
        while left <= right:
            if leftMax <= rightMax:
                result += max(0, leftMax-height[left])
                leftMax = max(leftMax, height[left])
                left += 1
            else:
                result += max(0, rightMax-height[right])
                rightMax = max(rightMax, height[right])
                right -= 1
        return result