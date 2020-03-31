class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 1. 手写
        lenA, lenB = len(a), len(b)
        ra, rb = a[::-1], b[::-1]
        i, carry = 0, 0
        res = ""
        while i < lenA and i < lenB:
            temp = int(ra[i]) + int(rb[i]) + carry
            if temp >= 2:
                res += str(temp - 2)
                carry = 1
            else:
                res += str(temp)
                carry = 0
            i += 1
        while i < lenA:
            temp = int(ra[i]) + carry
            if temp >= 2:
                res += str(temp - 2)
                carry = 1
            else:
                res += str(temp)
                carry = 0
            i += 1
        while i < lenB:
            temp = int(rb[i]) + carry
            if temp >= 2:
                res += str(temp - 2)
                carry = 1
            else:
                res += str(temp)
                carry = 0
            i += 1
        if carry == 1:
            res += "1"
        return res[::-1]

