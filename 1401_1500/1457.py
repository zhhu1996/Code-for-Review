# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        """二叉树中的伪回文路径
        1. 回溯生成二叉树的所有路径，存入列表中，逐个判断单个路径是否满足伪回文
        伪回文：统计字符的出现次数，奇数次的字符<=1才返回True

        2. 不用保存每条路径，用字典记录当前路径下出现过的所有字符，以及出现次数
        """
        self.path = []

        def judgeStr(nums):
            if len(nums) <= 1:
                return True
            table = defaultdict(int)
            count = 0
            for i in range(len(nums)):
                table[nums[i]] += 1
            for key, value in table.items():
                if value % 2 == 1:
                    count += 1
            if count <= 1:
                return True
            else:
                return False

        def getPath(root, path):
            if not root:
                return
            if not root.left and not root.right:
                path.append(root.val)
                self.path.append(path.copy())
                path.pop()
                return
            path.append(root.val)
            getPath(root.left, path)
            getPath(root.right, path)
            path.pop()

        getPath(root, [])
        cnt = 0
        for i in range(len(self.path)):
            if judgeStr(self.path[i]):
                cnt += 1
        return cnt



