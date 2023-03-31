# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         """
#         1. 动态规划: dp[i]表示以i结尾的最长子序列的长度
#         => dp[i] = max(dp[j]+1), j < i and a[i]>a[j]
#         """
#         # if not nums:
#         #     return 0
#         # dp = [1]
#         # for i in range(1, len(nums)):
#         #     result = 1
#         #     for j in range(i):
#         #         if nums[i] > nums[j]:
#         #             result = max(dp[j]+1, result)
#         #     dp.append(result)
#         # return max(dp)

#         """
#         2. 贪心+二分查找: https://leetcode.cn/problems/longest-increasing-subsequence/solutions/7196/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
#         => tail[i]表示长度为i+1的所有最长上升子序列的结尾的最小值, tail也是一个严格上升数组
#         遍历nums:
#         step1: 如果nums数组的当前元素严格大于tail的尾元素, 就添加到tail数组的末尾
#         step2: 在有序数组tail中查找第一个大于num的元素, 更新为num
#         """
#         if len(nums) <= 1:
#             return len(nums)
#         tail = [nums[0]]
#         for i in range(1, len(nums)):
#             if nums[i] > tail[-1]:
#                 tail.append(nums[i])
#                 continue
#             left, right = 0, len(tail)-1
#             while left < right:
#                 mid = (left + right) // 2
#                 if tail[mid] < nums[i]:
#                     left = mid + 1
#                 else:
#                     right = mid
#             tail[left] = nums[i]
#         return len(tail)

        # # 3. 贪心 + 二分, 时间复杂度O(nlogn)
        # # dp[i]: 长度为i+1的IS的末尾最小值
        # n = len(nums)
        # dp = [nums[0]]
        # for i in range(1, n):
        #     l, r = 0, len(dp)-1
        #     target = nums[i]
        #     while l <= r:
        #         mid = (l +  r) // 2
        #         # f(l-1)<target, f(r+1)>=target
        #         if dp[mid] < target:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     if l == len(dp):
        #         dp.append(nums[i])
        #     else:
        #         dp[l] = nums[i]
        # return len(dp)


class ArrayNode(object):
    def __init__(self, value, pre=None):
            """
                value: 数组单个元素
                pre: 该元素的前一个节点
            """
            self.value = value
            self.pre = pre

class LIS(object):
    def __init__(self, nums):
        self.nums = nums
        self.piles = []
        self.lis = []

    def gen_LIS(self):
        for i in range(len(self.nums)):
            if i == 0:
                self.piles.append([ArrayNode(self.nums[0])])
                continue
            target = self.nums[i]
            left, right = 0, len(self.piles)-1
            while left < right:
                mid = (left + right) // 2
                if self.piles[mid][-1].value <= target:
                    left = mid + 1
                else:
                    right = mid
            # print(left, self.nums[i])
            # i.left大于堆长 ii.目标值大于等于当前元素 => 新建堆
            if left >= len(self.piles) or target > self.piles[left][-1].value:
                left += 1
                self.piles.append([ArrayNode(target, self.piles[left-1][-1])])
            else: # 在目标堆上插入
                if left == 0:
                    self.piles[left].append(ArrayNode(target))
                else:
                    self.piles[left].append(ArrayNode(target, self.piles[left-1][-1]))
    

    def get_LIS_len(self):
        return len(self.piles)

    def get_LIS_combinations(self):
        def get_LIS_node(cnt, len, it, temp):
            """
                cnt: 遍历的节点数
                len: pile数
                it: 当前遍历的节点
                temp: 当前的最长递减子序列
            """
            # print(cnt, it.value, len)
            if not it:
                if cnt >= len-1:
                    self.lis.append(temp[::-1])
                return
            temp.append(it.value)
            get_LIS_node(cnt+1, len, it.pre, temp)
            temp.pop()

        for node in self.piles[-1]:
            if node.pre:
                get_LIS_node(0, len(self.piles), node, [])
        print('LIS combinations: ', self.lis)
        
    def print_top_values(self):
        print('top values:', end=' ')
        for i in range(len(self.piles)):
            print(self.piles[i][-1].value, end=' ')
        print()

    def print_level_values(self):
        links = []
        print()
        print('level visit:')
        for i in range(len(self.piles)):
            print(' level {}:'.format(i), end=' ')
            for node in self.piles[i]:
                print(node.value, end=' ')
                if node.pre:
                    links.append([node.pre.value, node.value])
            print()
        print('links: {}'.format(links))
        
            
test_nums = [6,3,5,10,11,2,9,14,13,7,4,8,12]
test_case = LIS(test_nums)
test_case.gen_LIS()
print('LIS length: {}'.format(test_case.get_LIS_len()))
print()
test_case.print_top_values()
test_case.print_level_values()  
print()            
test_case.get_LIS_combinations()
