class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        """三个有序数组的交集
        1. 先用双指针查找arr1与arr2的交集，再判断该元素是否在arr3，时间复杂度O(n1+n2),空间复杂度O(n3)
        """
        set3 = set(arr3)
        i, j = 0, 0
        result = []
        n1, n2 = len(arr1), len(arr2)
        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                if arr1[i] in set3:
                    result.append(arr1[i])
                i += 1
                j += 1
        return result