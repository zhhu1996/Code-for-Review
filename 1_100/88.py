class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # 1. 最简单的做法，直接调用库函数排序
        # nums1[m:m+n] = nums2[:n]
        # nums1.sort()

        # 2. 归并排序的partition函数，尾插入法
        pos = n + m - 1
        it1 = m - 1
        it2 = n - 1
        while it1 >= 0 and it2 >= 0:
            if nums1[it1] > nums2[it2]:
                nums1[pos] = nums1[it1]
                it1 -= 1
            else:
                nums1[pos] = nums2[it2]
                it2 -= 1
            pos -= 1
        if it1 >= 0:  # 序列1还没有比较完
            nums1[:pos + 1] = nums1[:it1 + 1]
        if it2 >= 0:  # 序列2还没有比较完
            nums1[:pos + 1] = nums2[:it2 + 1]