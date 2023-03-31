class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        """因子的组合
        1. 递归
        """
        def get_fac(i, n):
            fac = []
            while i * i <= n:
                if n % i == 0:
                    fac.append([i, n//i])
                    tmp = get_fac(i, n//i)
                    for t in tmp:
                        fac.append([i]+t)
                i += 1
            return fac

        return get_fac(2, n)