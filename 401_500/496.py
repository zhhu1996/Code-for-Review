class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """下一个更大元素 I
        方法一: 单调栈，时间复杂度O(m+n)，m为nums1大小，n为nums2大小
        遍历nums2，对每个元素的下一个更大元素，建立map映射
        维护一个单调递减的堆栈，每次插入新元素的时候，弹出栈中小于该元素的元素(这些被pop的元素找到了下一个更大的元素）
        """
        table = {}
        stack = []
        for i in range(len(nums2)):
            if not stack:
                stack.append(nums2[i])
                continue
            while stack and stack[-1] < nums2[i]:
                tmp = stack.pop(-1)
                table[tmp] = nums2[i]
            stack.append(nums2[i])
        while stack:
            table[stack.pop(-1)] = -1
        result = []
        for j in range(len(nums1)):
            result.append(table[nums1[j]])
        return result