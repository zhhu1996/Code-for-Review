class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """找到k个最接近的元素
        1. 先二分查找第一个大于等于x的数, 再搜索k个位置, 时间复杂度O(max(k, log(n)))

        2. 双指针, 时间复杂度O(n)

        3. 二分查找左边界, 时间复杂度O(logn)
        构造函数f(x) = t-nums[x]-(nums[x+k]-t)
        [l,r]上存在点p, 当x<p时,f(x) > 0; 当x>p时, f(x) <= 0, 满足二分性

        4. 滑动窗口, 时间复杂度O(n)
        """
        # # 1. 二分查找第一个大于等于x的数, 然后指针左右摆动直到满足条件
        # left, right = 0, len(arr)-1
        # while left < right:
        #     mid = (left + right) // 2
        #     if arr[mid] < x:
        #         left = mid + 1
        #     else:
        #         right = mid
        # # 寻找最接近x的值
        # if left > 0 and abs(arr[left-1]-x) <= abs(arr[left]-x):
        #     index = left - 1
        # else:
        #     index = left
        # # 左右扩张
        # cnt = 1
        # l, r = index, index
        # while cnt < k:
        #     if l > 0 and r < len(arr)-1:
        #         tl = arr[l-1]
        #         rl = arr[r+1]
        #     elif l > 0:
        #         l -= 1
        #         cnt += 1
        #         continue
        #     elif r < len(arr)-1:
        #         r += 1
        #         cnt += 1
        #         continue
        #     if abs(tl-x) <= abs(rl-x):
        #         l -= 1
        #     else:
        #         r += 1
        #     cnt += 1
        # return arr[l:r+1]


        # # 2. 双指针, 左指针指向左边界, 右指针指向右边界, 每次删除1个元素直到剩下k个元素就是结果
        # left, right = 0, len(arr)-1
        # while right - left + 1 > k:
        #     if abs(arr[right]-x) < abs(arr[left]-x):
        #         left += 1
        #     else:
        #         right -= 1
        # return arr[left: right+1]


        # 3.
        n = len(arr)
        l, r = 0, n-k
        # [l,r]上存在点p, 当x<p时, t-nums[x] > nums[x+k]-t; 当x>=p时, t-nums[x] <= nums[x+k]-t
        while l <= r:
            mid = (l + r) // 2
            # f(l-1) > 0, f(r+1) <= 0
            if mid+k < n and x-arr[mid] > arr[mid+k]-x:
                l = mid + 1
            else:
                r = mid - 1
        return arr[l: l+k]