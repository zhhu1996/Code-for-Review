class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        """最小无法得到的或值
        1. 位运算
        从小到大枚举2^i是否出现过, 第一个没出现的就是答案
        """
        e = set(nums)
        i = 0
        while True:
            num = 2 ** i
            if num not in e:
                return num
            i += 1