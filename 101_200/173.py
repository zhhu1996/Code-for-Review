# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """二叉搜索树迭代器
    1. 一次性生成中序遍历的列表，后用索引遍历

    2. 用堆栈模拟生成中序列表
    """

    def __init__(self, root: TreeNode):
        self.stack = []
        self.root = root


    def next(self) -> int:
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        self.root = self.stack.pop()
        result = self.root.val
        self.root = self.root.right
        return result

    def hasNext(self) -> bool:
        if not self.root and not self.stack:
            return False
        return True



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()