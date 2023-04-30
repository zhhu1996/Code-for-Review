class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """字符串相加
        1. 迭代
        反转字符串, 逐一计算
        """
        s1 = num1[::-1]
        s2 = num2[::-1]
        m, n = len(s1), len(s2)
        i, j, carry = 0, 0, 0
        ans = []
        while i < m and j < n:
            num = int(s1[i]) + int(s2[j]) + carry
            carry = num // 10
            num = num % 10
            ans.append(str(num))
            i += 1
            j += 1
        while i < m:
            num = int(s1[i]) + carry
            carry = num // 10
            num = num % 10
            ans.append(str(num))
            i += 1
        while j < n:
            num = int(s2[j]) + carry
            carry = num // 10
            num = num % 10
            ans.append(str(num))
            j += 1
        if carry > 0:
            ans.append(str(carry))
        return ''.join(ans[::-1])