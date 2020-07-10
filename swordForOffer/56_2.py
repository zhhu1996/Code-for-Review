class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """数组中唯一只出现一次的数字，其他数字均出现了3次
        将每个数字转换成二进制，并将二进制的每一位相加，得到一个32个元素的数组；
        如果某一位的和能够被3整除，说明那唯一的数字这一位为0，否则就是1；
        逐个遍历数组，就能得到唯一数字的32位二进制表示
        """
        bitNums = [0 for i in range(32)]
        for i in range(len(nums)):
            for j in range(32):
                bit = (nums[i] >> j) & 1
                bitNums[j] += bit
        result = 0
        for j in range(32):
            result = result << 1
            result += bitNums[31 - j] % 3
        return result