class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        """循环码排列
        1. 二进制编码->格雷码
        二进制: Bn-1Bn-2...B0
        格雷码: Gn-1Gn-2...G0
        Gn-1 = Bn-1, Gi = Bi+1 ^ Bi
        """
        grays = [i ^ (i>>1)  for i in range(1<<n)]
        k = grays.index(start)
        return grays[k:] + grays[:k]