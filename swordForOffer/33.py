class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        """
        1. 后序遍历 + 中序遍历确定是否是一棵二叉搜索树
        2. 直接根据后序遍历来判断: 右子树中出现>根节点的值即可返回False
        """

        def isBST(inorder, postorder):
            if not inorder and not postorder:
                return True
            if not inorder or not postorder:
                return False
            if postorder[-1] not in inorder:
                return False
            else:
                rootIndex = inorder.index(postorder[-1])
                return isBST(inorder[: rootIndex], postorder[: rootIndex]) and isBST(inorder[rootIndex + 1:],
                                                                                     postorder[rootIndex: -1])

        def isBSTV2(postorder):
            if not postorder:
                return True
            i = 0
            rootvalue = postorder[-1]
            while i < len(postorder) - 1:
                if postorder[i] < rootvalue:
                    i += 1
                else:
                    break
            leftorder, rightorder = postorder[: i], postorder[i: -1]
            for j in range(i, len(postorder)-1):
                if postorder[j] <= rootvalue:
                    return False
            return isBSTV2(leftorder) and isBSTV2(rightorder)

        # inorder = list(sorted(postorder))
        # return isBST(inorder, postorder)
        return isBSTV2(postorder)
