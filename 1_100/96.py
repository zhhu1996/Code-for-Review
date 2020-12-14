class Solution:
    def numTrees(self, n: int) -> int:
        """f(n)表示n个元素可组成的二叉搜索树的个数
        f(i) = sum(f(i-1)*f(n-i))
        """
        if n <= 1:
            return 1
        f = [1, 1]
        for i in range(2, n+1):
            temp = 0
            for j in range(1, i+1):
                temp += f[j-1] * f[i-j]
            f.append(temp)
        return f[-1]
