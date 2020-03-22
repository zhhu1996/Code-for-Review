class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1. set
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)

        # 2. 排序+双指针

        # 3. 排序+二分查找