class Solution:
    def findNthDigit(self, n: int) -> int:
        """数字序列中的某一位
        """

        def countBits(digits):
            if digits == 1:
                return 10
            base = 1
            for i in range(digits-1):
                base *= 10
            return base * 9 * digits

        def findIndex(index, digits):
            if digits < 1:
                return -1
            if digits == 1:
                begin = 0
            else:
                begin = 10 ** (digits-1)
            number = begin + index // digits
            indexFromR = digits - index % digits
            for i in range(indexFromR):
                number /= 10
            return number

        if n < 0:
            return -1
        digits = 1
        while True:
            numbers = countBits(digits)
            if n < numbers:
                return findIndex(n, digits)
            n -= numbers
            digits += 1