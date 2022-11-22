class Solution:
    def reverseBits(self, n: int) -> int:
        tmp = []
        res = 0
        while n > 0:
            bit = n % 2
            tmp.append(bit)
            n = n // 2
        if len(tmp) < 32:
            tmp.extend([0]*(32-len(tmp)))
        for i in range(len(tmp)):
            res = res * 2 + tmp[i]
        return res