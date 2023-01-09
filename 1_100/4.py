class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # # 1. 遍历求第k小：时间复杂度O(m+n)，空间复杂度O(1)
        # m, n = len(nums1), len(nums2)
        # mid = (m + n) // 2
        # i, j, k = 0, 0, 0
        # left, right = -1, -1
        # while k <= mid:
        #     left = right
        #     if (i < m and j < n and nums1[i] < nums2[j]) or (j >= n):
        #         right = nums1[i]
        #         i += 1
        #     else:
        #         right = nums2[j]
        #         j += 1
        #     k += 1
        # if (m + n) % 2 == 0:
        #     return (left + right) / 2
        # else:
        #     return right 

        # 2. 二分查找求第k小: 时间复杂度O(log(m+n))
        def getKth(arr1, arr2, k):
            # 递归出口
                # i.    k <= 1
                # ii.   k > 1 && arr1 = []
                # iii.  k > 1 && arr2 = []
            if k <= 1: 
                if arr1 and arr2:
                    return min(arr1[0], arr2[0])
                elif arr1:
                    return arr1[0]
                else:
                    return arr2[0]
            if len(arr1) == 0: 
                return arr2[k-1]
            if len(arr2) == 0: 
                return arr1[k-1]
            # 二分查找
            mid = k // 2 - 1
            # 考虑中点大于数组长度，否则会导致数组越界
            i1 = min(mid, len(arr1)-1)
            i2 = min(mid, len(arr2)-1)
            if arr1[i1] < arr2[i2]:
                return getKth(arr1[i1+1:], arr2, k-i1-1)
            else:
                return getKth(arr1, arr2[i2+1:], k-i2-1)

        l = len(nums1)+len(nums2)
        if l % 2 == 1:
            return getKth(nums1, nums2, l//2+1)
        else:
            return (getKth(nums1, nums2, l//2) + getKth(nums1, nums2, l//2+1)) / 2
