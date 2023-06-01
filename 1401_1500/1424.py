class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """对角线遍历II
        1. 层序遍历

        2. 哈希: 利用对角线性质进行聚类
        反对角线上元素之和相等, 对角线上元素之差相等
        """ 
        # # 1.      
        # from collections import deque

        # if not nums: return []
        # q = deque()
        # m, ans, visit = len(nums), [], set()
        # q.append((0,0))
        # visit.add((0,0))
        # while q:
        #     size = len(q)
        #     for i in range(size):
        #         x, y = q.popleft()
        #         ans.append(nums[x][y])
        #         if x+1 < m and y < len(nums[x+1]) and (x+1, y) not in visit:
        #             q.append((x+1, y))
        #             visit.add((x+1, y))
        #         if y+1 < len(nums[x]) and (x, y+1) not in visit:
        #             q.append((x, y+1))
        #             visit.add((x, y+1))
        # return ans


        # 2.
        hm = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                key = i + j
                hm[key].append(nums[i][j])
        ans = []
        for k, v in sorted(hm.items(), key=lambda x: x[0]):
            ans.extend(v[::-1])
        return ans