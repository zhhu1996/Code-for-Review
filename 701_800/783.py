# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        """二叉搜索树节点最小距离
        1. 中序遍历得到顺序数组，求相差最小的两节点

        2. 中序遍历的同时保存前一个节点，求相邻节点的差值
        """
        # 方法1
        # self.order = []
        #
        # def inOrder(root):
        #     if not root:
        #         return
        #     inOrder(root.left)
        #     self.order.append(root.val)
        #     inOrder(root.right)
        #
        # inOrder(root)
        # minValue = float("inf")
        # n = len(self.order)
        # for i in range(n - 1):
        #     if i == 0:
        #         minValue = min(minValue, abs(self.order[i] - self.order[i + 1]))
        #     else:
        #         minValue = min(minValue, abs(self.order[i] - self.order[i - 1]), abs(self.order[i] - self.order[i + 1]))
        # return minValue

        # 方法2
        def inOrder(root):
            if root:
                inOrder(root.left)
                if self.preNode:
                    self.result = min(self.result, abs(root.val-self.preNode.val))
                self.preNode = root
                inOrder(root.right)


        self.result = float("inf")
        self.preNode = None
        inOrder(root)
        return self.result
