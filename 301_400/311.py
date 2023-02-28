class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        """稀疏矩阵的乘法
        1. 暴力
        c[i][j] = a[i][:] * b[:][j]

        2. 利用稀疏矩阵的性质建立哈希表
        """
        # # 1.
        # m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        # mat3 = [[0 for i in range(n)] for j in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         mij = 0
        #         for t in range(k):
        #             mij += mat1[i][t] * mat2[t][j]
        #         mat3[i][j] = mij
        # return mat3

        # 2.  
        map1, map2 = {}, {}
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        mat3 = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:
                    if i not in map1:
                        map1[i] = {j: mat1[i][j]}
                    else:
                        map1[i][j] = mat1[i][j]
        for i in range(k):
            for j in range(n):
                if mat2[i][j] != 0:
                    if j not in map2:
                        map2[j] = {i: mat2[i][j]}
                    else:
                        map2[j][i] = mat2[i][j]
        for i in range(m):
            if i not in map1:
                continue
            for j in range(n):
                if j not in map2:
                    continue
                mij = 0
                for k1, v1 in map1[i].items():
                    if k1 in map2[j]:
                        mij += v1 * map2[j][k1]
                mat3[i][j] = mij
        return mat3