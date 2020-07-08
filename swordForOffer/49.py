class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """丑数
        1. 暴力：对每个数字都判断是否是丑数，太费时间

        2. 根据之前的丑数动态地生成下一个丑数
        """
        uglyNumber = [1]
        if n <= 1:
            return 1
        j, k, l = 0, 0, 0
        for i in range(1, n+1):
            while uglyNumber[j] * 2 <= uglyNumber[i-1]:
                j += 1
            while uglyNumber[k] * 3 <= uglyNumber[i-1]:
                k += 1
            while uglyNumber[l] * 5 <= uglyNumber[i-1]:
                l += 1
            nextUglyNumber = min(uglyNumber[j] * 2, uglyNumber[k] * 3, uglyNumber[l] * 5)
            uglyNumber.append(nextUglyNumber)
        return uglyNumber[n-1]