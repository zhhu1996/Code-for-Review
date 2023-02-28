# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """从前序与中序遍历序列构造二叉树
        先序遍历: 根、左子树、右子树
        中序遍历: 左子树、根、右子树
        """
        def buildTreeNode(preorder, inorder, pl, pr, il, ir):
            # 根据preorder[pl..pr]与inorder[il..ir]构建子树
            if pl > pr: return None
            target = preorder[pl]
            root = TreeNode(target)
            i = il
            while i <= ir:
                if inorder[i] == target:
                    break
                i += 1
            cnt = i - il
            root.left = buildTreeNode(preorder, inorder, pl+1, pl+1+cnt-1, il, i-1)
            root.right = buildTreeNode(preorder, inorder, pl+1+cnt, pr, i+1, ir)
            return root

        return buildTreeNode(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)