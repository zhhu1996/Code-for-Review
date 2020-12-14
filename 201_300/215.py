class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """数组中第k大的元素
        基于partition函数进行快排
        """
        def partition(array, start, end):
            index = start - 1
            while start < end:
                if array[start] > array[end]:
                    index += 1
                    array[index], array[start] = array[start], array[index]
                start += 1
            index += 1
            array[index], array[end] = array[end], array[index]
            return index

        begin, end = 0, len(nums) - 1
        index = partition(nums, begin, end)
        while index != k - 1:
            if index < k - 1:
                begin = index + 1
            else:
                end = index - 1
            index = partition(nums, begin, end)
        return nums[index]

