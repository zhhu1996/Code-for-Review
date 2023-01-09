class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        寻找满足arr[0] < arr[1] < ... < arr[i-1] < arr[i] > arr[i+1] > ... > arr[len-1]的下标i,
        => 第一个小于前元素的索引
        """
        left, right = 0, len(arr)-1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid-1]:
                left = mid + 1
            else:
                right = mid
        return left-1