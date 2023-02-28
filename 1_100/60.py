class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 1. 无重复元素，类似于全排列，然后求第k个排列，时间复杂度O(n!)，超时
        # check = [0] * (n + 1)
        # self.res = []
        #
        # def calcPermutation(n, index, temp):
        #     if index == n:
        #         self.res.append(temp.copy())
        #         return
        #     for i in range(1, n + 1):
        #         if check[i] == 1:
        #             continue
        #         check[i] = 1
        #         temp.append(i)
        #         calcPermutation(n, index + 1, temp)
        #         temp.pop()
        #         check[i] = 0
        #
        # calcPermutation(n, 0, [])
        # maxLen = 1
        # for i in range(1, n + 1):
        #     maxLen *= i
        # if k < maxLen:
        #     target = k - 1
        # else:
        #     target = -1
        # return "".join([str(c) for c in self.res[target]])

        # # 2. k-1=an*(n-1)!+an-1*(n-2)!+....+a1*0!
        # # https://leetcode-cn.com/problems/permutation-sequence/solution/kang-tuo-bian-ma-by-rayyi-2/
        # f = [1 for i in range(0,n+1)]
        # res = ""
        # array = [i for i in range(1, n+1)]
        # for i in range(2, n+1):
        #     f[i] = f[i-1] * i
        # k -= 1
        # for i in range(n, 0, -1):
        #     a = k // f[i-1]
        #     k = k % f[i-1]
        #     res += str(array[a])
        #     array.pop(a)
        # return "".join(res)

        # 3.
        def dfs(n, k, index, path):
            """
                n: 候选集[1, n]
                k: 待搜索的第k个排列
                index: 已使用的数字个数
                path: 当前路径
            """
            if index == n:
                return
            cnt = fab[n-index-1] # 当前层的排列数
            for i in range(1, n+1):
                if visit[i]:
                    continue
                if k > cnt:
                    k -= cnt
                    continue
                visit[i] = True
                path.append(i)
                dfs(n, k, index+1, path)
                return

        if n == 0:
            return ''
        visit = [False for _ in range(n+1)]
        fab = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            fab[i] = fab[i-1] * i
        res = []
        dfs(n, k, 0, res)
        return ''.join([str(num) for num in res])


