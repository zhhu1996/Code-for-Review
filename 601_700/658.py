class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # # 1. 排除法: https://leetcode-cn.com/problems/find-k-closest-elements/solution/pai-chu-fa-shuang-zhi-zhen-er-fen-fa-python-dai-ma/
        # left, right = 0, len(arr)-1
        # n = len(arr)
        # while n > k:
        #     if x - arr[left] < arr[right] - x:
        #         right -= 1
        #     elif x - arr[left] > arr[right] - x:
        #         left += 1
        #     else:
        #         right -= 1
        #     n -= 1
        # return arr[left: right+1]

        # 2. 二分查找法
        """
        x不在[mid, mid+k]
            i. x在mid左边 -> right = mid
            ii.x在mid+k右边 -> left = mid + 1
        x在[mid, mid+k]
            i. x距离mid更近 -> right = mid
            ii. x距离mid+k更近 -> left = mid + 1
        """
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] <= arr[mid+k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left: left+k]
