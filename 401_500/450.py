# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """删除二叉搜索树中的节点
        1. 递归搜索, 时间复杂度O(h), h=树高, 该方法会增加树的高度
            i.  当前值小于key, 则去右子树中搜索
            ii. 当前值大于key, 则去左子树中搜索
            iii.当前值等于key, 对当前子树进行调整: 寻找右子树的最小节点, 将左子树连接到该节点的左孩子上
        2. 递归搜索, 时间复杂度O(h), h=树高, 该方法不会增加树的高度
            i.  当前值小于key, 则去右子树中搜索
            ii. 当前值大于key, 则去左子树中搜索
            iii.当前值等于key, 对当前子树进行调整: 寻找右子树的最小节点/左子树的最大节点
        3. 迭代搜索
        """
        # # 1.
        # if not root: return None
        # if root.val < key:
        #     root.right = self.deleteNode(root.right, key)
        # elif root.val > key:
        #     root.left = self.deleteNode(root.left, key)
        # else:
        #     if not root.right:
        #         return root.left
        #     cur = root.right
        #     while cur and cur.left:
        #         cur = cur.left
        #     cur.left = root.left
        #     return root.right
        # return root


        # 2.
        if not root: return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.right: # 寻找右子树的最小节点
                cur = root.right
                while cur and cur.left:
                    cur = cur.left
                # root.val = cur.val
                # root.right = self.deleteNode(root.right, cur.val)
                cur.right = self.deleteNode(root.right, cur.val)
                cur.left = root.left
            elif root.left: # 寻找左子树的最大节点
                cur = root.left
                while cur and cur.right:
                    cur = cur.right
                # root.val = cur.val
                # root.left = self.deleteNode(root.left, cur.val)
                cur.left = self.deleteNode(root.left, cur.val)
                cur.right = root.right
            else:
                # root = None
                cur = None
            # return root
            return cur
        return root