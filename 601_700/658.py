class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 1. 排除法: https://leetcode-cn.com/problems/find-k-closest-elements/solution/pai-chu-fa-shuang-zhi-zhen-er-fen-fa-python-dai-ma/
        left, right = 0, len(arr)-1
        n = len(arr)
        while n > k:
            if abs(arr[left]-x) < abs(arr[right]-x):
                right -= 1
            elif abs(arr[left]-x) > abs(arr[right]-x):
                left += 1
            else:
                right -= 1
            n -= 1
        return arr[left: right+1]