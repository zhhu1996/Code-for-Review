class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """数字范围按位与
        1. LCS
        移位求left和right的LCS

        2. Brian Kernighan算法
        通过n & (n-1)去除最右位的1
        """
        # # 1.
        # offset = 0
        # while left < right:
        #     left = left >> 1
        #     right = right >> 1
        #     offset += 1
        # return left << offset

        # 2.
        while left < right:
            right = right & (right - 1)
        return right