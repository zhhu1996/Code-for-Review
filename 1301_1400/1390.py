import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        if not nums:
            return 0

        def calcDivisor(number):
            res = set()
            for i in range(1, int(math.sqrt(number))+1):
                if number % i == 0:
                    res.add(i)
                    res.add(number//i)
            return list(res)

        cntMap = {}
        result = 0
        for num in nums:
            cntMap[num] = calcDivisor(num)
            if len(cntMap[num]) == 4:
                result += sum(cntMap[num])

        return result