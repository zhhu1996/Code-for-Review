class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """数组中的逆序对
        1. 遍历所有的数对，判断是否是逆序，时间复杂度O(n^2)

        2. 不能将某个数字和它之后的所有数字进行比较，否则时间复杂度就是平方级，每次只比较相邻两个元素，记录下逆序数，然后返回排序后的数组
        """

        self.result = 0

        def binarayArray(nums):
            # 归并排序
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = binarayArray(nums[:mid])
            right = binarayArray(nums[mid:])
            sortArray = [-1 for i in range(len(nums))]
            leftIndex, rightIndex, sortIndex = len(left) - 1, len(right) - 1, len(sortArray) - 1
            while leftIndex >= 0 and rightIndex >= 0:
                if left[leftIndex] > right[rightIndex]:
                    self.result += rightIndex + 1
                    sortArray[sortIndex] = left[leftIndex]
                    leftIndex -= 1
                    sortIndex -= 1
                else:
                    sortArray[sortIndex] = right[rightIndex]
                    rightIndex -= 1
                    sortIndex -= 1
            while leftIndex >= 0:
                sortArray[sortIndex] = left[leftIndex]
                leftIndex -= 1
                sortIndex -= 1
            while rightIndex >= 0:
                sortArray[sortIndex] = right[rightIndex]
                rightIndex -= 1
                sortIndex -= 1
            return sortArray

        binarayArray(nums)
        return self.result