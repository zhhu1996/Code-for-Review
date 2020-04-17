class Solution:
    def numTrees(self, n: int) -> int:
        # 1. 动态规划
        # g(i)表示i个节点存在二叉排序树的个数，f(i)表示以i为根的二叉搜索树的个数
        # g(i) = sum(f(j))，g(i)等于以1，2...i为根节点的二叉搜索树的个数相加
        # f(j) = g(j-1) * g(i-j)，f(j)等于左子树的可能*右子树的可能，g(j-1)表示左子树，g(i-j)表示右子树的可能
        # 所以g(i) = sum(g(j-1)*g(i-j))
        g = [0] * (n + 1)
        g[0] = 1
        g[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                g[i] += g[j - 1] * g[i - j]

        return g[n]