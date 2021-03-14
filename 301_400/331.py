class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """验证二叉树的前序序列化
        方法一:
        每个元素对应两个子节点，在新的非空节点插入时，遍历之前的所有节点，需要存在某一个节点的孩子节点小于两个
        """
        # 方法一
        if not preorder:
            return True
        preorder = preorder.split(',')
        cnt = [0 for i in range(len(preorder))]
        if len(preorder) == 1 and preorder[0] == '#':
            return True
        for i in range(len(preorder)):
            if i == 0 and preorder[i] != '#':
                continue
            flag = True
            for j in range(i - 1, -1, -1):
                if preorder[j] != '#' and cnt[j] < 2:
                    flag = False
                    cnt[j] += 1
                    break
            if flag:
                return False
        for i in range(len(preorder)):
            if preorder[i] != '#' and cnt[i] < 2:
                return False
        return True

