class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 1. 暴力回溯
        # self.res = []
        # self.codeTable = {}
        #
        # def calcCode(index, codeList, n):
        #     nowCode = codeList[-1]
        #     if nowCode in self.codeTable:
        #         return
        #     else:
        #         self.codeTable[nowCode] = 1
        #
        #     if index == n-1:
        #         self.res = codeList.copy()
        #         return
        #
        #     for i in range(len(nowCode)):
        #         nextCode = nowCode[:i] + str(abs(1 - int(nowCode[i]))) + nowCode[i+1:]
        #         codeList.append(nextCode)
        #         calcCode(index+1, codeList, n)
        #         codeList.pop()
        #
        # def binary2int(string):
        #     base = 1
        #     res = 0
        #     for i in range(len(string)-1, -1, -1):
        #         res += base * int(string[i])
        #         base *= 2
        #     return res
        #
        # calcCode(0, ['0'*n], math.pow(2,n))
        # return list(map(lambda x: binary2int(x), self.res))

        # 2. 迭代法, G(n+1) = G(n) | (倒序的G(n)，首位添加1)
        res = [0]
        for i in range(n):
            add = 1 << i
            for j in range(len(res)-1, -1, -1):
                res.append(res[j] + add)
        return res