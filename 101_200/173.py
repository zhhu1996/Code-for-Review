# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """二叉搜索树迭代器
    1. 预处理, 时间复杂度O(n), 空间复杂度O(n)
    预处理生成递增序列, 再依据当前指针取值

    2. 转换成有序链表, 时间复杂度O(n), 不需要额外空间
    """
    def __init__(self, root: Optional[TreeNode]):
        self.dummy = TreeNode(-1)
        self.pre = self.dummy
        self.cur = self.dummy
        self.to_list(root)

    def next(self) -> int:
        if not self.hasNext():
            return -1
        self.cur = self.cur.right
        return self.cur.val

    def hasNext(self) -> bool:
        return self.cur is not None and self.cur.right is not None

    def to_list(self, root):
        if not root: return
        self.to_list(root.left)
        self.pre.right = root
        root.left = self.pre
        self.pre = root
        self.to_list(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()