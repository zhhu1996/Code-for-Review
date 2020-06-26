# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """递归生成"""

        def buildTreeCore(preorder, inorder):
            """将数组复制作为参数传递"""
            if not preorder or not inorder:
                return None

            rootValue = preorder[0]
            root = TreeNode(rootValue)
            i = 0
            while i < len(inorder):
                if inorder[i] == rootValue:
                    break
                i += 1
            root.left = buildTreeCore(preorder[1: 1+i], inorder[: i])
            root.right = buildTreeCore(preorder[1+i:], inorder[i+1:])
            return root

        def buildTreeCoreV2(preorder, inorder, prestart, preend, instart, inend):
            """不复制数组，传索引作为参数"""
            if prestart > preend or instart > inend: # 递归出口
                return None

            rootValue = preorder[prestart]
            root = TreeNode(rootValue)
            i = instart
            while i <= inend:
                if inorder[i] == rootValue:
                    break
                i += 1
            root.left = buildTreeCoreV2(preorder, inorder, prestart+1, prestart+i-instart, instart, i-1)
            root.right = buildTreeCoreV2(preorder, inorder, prestart+1+i-instart, preend, i+1, inend)
            return root


        # return buildTreeCore(preorder, inorder)
        return buildTreeCoreV2(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)