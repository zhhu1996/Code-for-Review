class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """验证二叉树的前序序列化
        1. 每个元素对应两个子节点，在新的非空节点插入时，遍历之前的所有节点，需要存在某一个节点的孩子节点小于两个

        2. 不重构树: 判读每个位置下剩余边的数量, 遍历完成前减为0即为非法
            9 -> 2
            9,3 -> 3
            9,3,4 -> 4
            9.3.4.# -> 3
            9,3,4,#,# -> 2
            9,3,4,#,#,1 -> 3
            9,3,4,#,#,1,# -> 2
            9,3,4,#,#,1,#,# -> 1
            9,3,4,#,#,1,#,#,2 -> 2
            ...
        """
        # # 1.
        # if not preorder:
        #     return True
        # preorder = preorder.split(',')
        # cnt = [0 for i in range(len(preorder))]
        # if len(preorder) == 1 and preorder[0] == '#':
        #     return True
        # for i in range(len(preorder)):
        #     if i == 0 and preorder[i] != '#':
        #         continue
        #     flag = True
        #     for j in range(i - 1, -1, -1):
        #         if preorder[j] != '#' and cnt[j] < 2:
        #             flag = False
        #             cnt[j] += 1
        #             break
        #     if flag:
        #         return False
        # for i in range(len(preorder)):
        #     if preorder[i] != '#' and cnt[i] < 2:
        #         return False
        # return True

        # 2.
        pre_list = preorder.split(',')
        n = len(pre_list)
        if n == 1:
            return pre_list[0] == '#'
        cnt = 0
        i = 0
        while i < n:
            if pre_list[i] != '#':
                if i == 0:
                    cnt += 2
                else:
                    cnt += 1
            else:
                cnt -= 1
            i += 1
            if cnt == 0:
                break
        if cnt != 0:
            return False
        return i == n
