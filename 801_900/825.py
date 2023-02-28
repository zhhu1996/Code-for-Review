class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        """适龄的朋友
        x->y: age[y] > 0.5*age[x] + 7 and age[y] <= age[x] and (age[y] <= 100 or age[x] >= 100)
        1. 两次二分查找, 时间复杂度O(nlogn)
        从x的角度看, 第一次bs查找满足条件的y, 第二次bs查找满足条件的同龄人

        2. 排序+双指针
        从y的角度看, [i,j)维护一个满足条件的x区间
        """
        # # 1.
        # n = len(ages)
        # cnt = 0
        # ages.sort()
        # for i in range(n-1, -1, -1):
        #     left, right = 0, i # left指向y, right指向x
        #     target = ages[i]
        #     while left < right:
        #         mid = (left + right) // 2
        #         if ages[mid] <= 0.5*target + 7:
        #             left = mid + 1
        #         else:
        #             right = mid
        #     if left < i and ages[left] > 0.5*target + 7:
        #         cnt += (i-left)
        #     if target > target*0.5 + 7:
        #         left, right = 0, i
        #         while left < right:
        #             mid = (left + right) // 2
        #             if ages[mid] < target:
        #                 left = mid + 1
        #             else:
        #                 right = mid
        #         if left < i and ages[left] == target:
        #             cnt += (i-left)
        # return cnt

        # 2. 
        def is_valid(x, y):
            if y <= 0.5*x + 7: return False
            if y > x: return False
            if y > 100 and x < 100: return False
            return True

        i, j, n = 0, 0, len(ages)
        cnt = 0
        ages.sort()
        for k in range(n):
            while i < k and not is_valid(ages[i], ages[k]): i+=1
            if j < k: j = k
            while j < n and is_valid(ages[j], ages[k]): j+=1
            if j > i: 
                cnt += j-i-1
        return cnt