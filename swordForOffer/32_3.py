# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """之字形层序遍历：需要用两个堆栈,
        从左向右打印：先压入左子节点，后压入右子节点
        从右向左打印：先压入右子节点，后压入左子节点
        """
        if not root:
            return []
        stack1, stack2 = [], []
        result, thisResult = [], []
        k = 1
        stack1.append(root)
        while stack1 or stack2:
            if k % 2 != 0:
                temp = stack1.pop()
                thisResult.append(temp.val)
                if temp.left:
                    stack2.append(temp.left)
                if temp.right:
                    stack2.append(temp.right)
                if not stack1:
                    k += 1
                    result.append(thisResult)
                    thisResult = []
            else:
                temp = stack2.pop()
                thisResult.append(temp.val)
                if temp.right:
                    stack1.append(temp.right)
                if temp.left:
                    stack1.append(temp.left)
                if not stack2:
                    k += 1
                    result.append(thisResult)
                    thisResult = []
        return result
