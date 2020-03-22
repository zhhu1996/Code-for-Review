class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1. 暴力求解, 大于O(n^2)
        # result = []
        # for i in nums1:
        #     if i in nums2:
        #         result.append(i)
        #         nums2.remove(i)
        # return result

        # 2. 排序+双指针，时间复杂度O(nlogn)
        # nums1.sort()
        # nums2.sort()
        # result = []
        # i, j = 0, 0
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] == nums2[j]:
        #         result.append(nums1[i])
        #         i += 1
        #         j += 1
        #     elif nums1[i] > nums2[j]:
        #         j += 1
        #     else:
        #         i += 1
        # return result

        # 3. 利用hash表存储每个数字出现的次数, 时间复杂度O(n)，空间复杂度O(n)
        if not nums1 or not nums2:
            return []
        result = []
        dict1 = dict()
        for i in nums1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        for i in nums2:
            if i in dict1 and dict1[i] > 0:
                result.append(i)
                dict1[i] -= 1
        return result