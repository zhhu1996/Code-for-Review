class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1. 暴力遍历，时间复杂度O(n^2)，超时

        # 2. 二分查找法，遍历每个 nums[i]，在剩余数组中查找 target-nums[i] 的值，时间复杂度O(nlogn)
        # def binarySearch(array, number):
        #     l, r = 0, len(array)-1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if array[mid] == number:
        #             return mid
        #         elif array[mid] < number:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     return -1
        #
        # for i in range(len(numbers)):
        #     result = binarySearch(numbers[i+1:], target-numbers[i])
        #     if result >= 0:
        #         return [i+1, i+2+result]

        # 3. 对撞指针法, 一个指向数组的开始，一个指向数组的结束，根据两个元素之和来不断的调整指针的位置
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1