class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """删除最短的子数组使剩余数组有序
        1. 双指针 + 二分, 时间复杂度O(nlogn)
        先通过双指针找到非递减区间arr[0..i1], arr[i2..n-1], 遍历arr[0..i1], 二分查找最长子数组

        2. 双指针, 时间复杂度O(n)
        先找到非递减区间arr[r..n-1], 然后双指针遍历寻找最长子数组
        """
        # # 1.
        # n = len(arr)
        # # 双指针: arr[0..i1], arr[i2..n-1]均为非递减
        # i1, i2 = 0, n-1
        # while i1 + 1 < n and arr[i1] <= arr[i1+1]:
        #     i1 += 1
        # while i2 - 1 >= 0 and arr[i2-1] <= arr[i2]:
        #     i2 -= 1
        # if i1 >= i2:
        #     return 0
        # # 二分: 搜索>=target的第一个元素
        # max_l = n-i2
        # for i in range(i1, -1, -1):
        #     l, r = i2, n-1
        #     target = arr[i]
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if arr[mid] < target:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     # f(l) >= target
        #     max_l = max(max_l, i+1+n-l)
        # return n-max_l


        # 2.
        n = len(arr)
        l, r = 0, n-1
        # arr[r..n-1] 非递减
        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1
        if r == 0: 
            return 0
        ans = r
        while l == 0 or arr[l-1] <= arr[l]:
            while r < n and arr[r] < arr[l]:
                r += 1
            ans = min(ans, r-l-1)
            l += 1
        return ans