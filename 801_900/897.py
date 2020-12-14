# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """递增顺序查找树
        1. 中序遍历生成序列，从最后一个节点开始，前一个节点的右孩子指向后一个节点

        2. 右、根、左的顺序
        用全局变量记录当前节点的后一个节点, 逐个处理右孩子；最后再设置左孩子为空，否则会构成环

        3. 左、根、右 中序遍历
        可以在递归的时候同时处理左右孩子，比方法2快
        """
        # # 方法1
        #
        # # 方法2
        # self.post = None
        #
        # def order(root):
        #     if not root:
        #         return None
        #
        #     order(root.right)
        #     root.right = self.post
        #     self.post = root
        #     order(root.left)
        #
        # order(root)
        # cur = self.post
        # while cur:
        #     cur.left = None
        #     cur = cur.right
        # return self.post

        # 方法3
        self.pre = TreeNode(-1)

        def inOrder(root):
            if not root:
                return

            inOrder(root.left)
            root.left = None
            self.pre.right = root
            self.pre = root
            inOrder(root.right)

        cur = self.pre
        inOrder(root)
        return cur.right
