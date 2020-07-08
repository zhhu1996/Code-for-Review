class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        """数组中数字出现的次数，要求时间复杂度O(n)，空间复杂度O(1)
        1. 先考虑数组中只有一个数字出现1次，其他都出现2次的情况：
        异或操作性质:
            x ^ x = 0
            x ^ 0 = x
        异或操作具有交换律和结合律，所以将数组中全部数字异或，最后得到的就是只出现一次的数字

        2. 再考虑数组中有两个出现1次的数字，其他数字都出现了2次。关键问题即是如何将这两个只出现1次的数字划分到两个数组中，并且这两个数组
        中其他数字也要成对划分，不能出现某一对数字不在一组的情况:
        先全部异或，得到不同的两个数字的异或结果；
        根据结果中第i位是否为1将全部数字分为满足条件的两组；
        之后对两组都进行异或操作即可
        """
        totalNum = 0
        singleNums = [0, 0]
        for i in range(len(nums)):
            totalNum = totalNum ^ nums[i]

        def getMoveBits(number):
            result = 0
            while number & 1 == 0:
                number = number >> 1
                result += 1
            return result

        moveBits = getMoveBits(totalNum)
        for i in range(len(nums)):
            if (nums[i] >> moveBits) & 1:
                singleNums[0] = singleNums[0] ^ nums[i]
            else:
                singleNums[1] = singleNums[1] ^ nums[i]
        return singleNums