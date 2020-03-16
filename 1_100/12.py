class Solution:
    def intToRoman(self, num: int) -> str:
        # 基于贪心的思想，每次拿最大值去匹配～
        res = ''
        dic = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
               4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        for k, v in sorted(dic.items(), key=lambda x: x[0], reverse=True):
            while num >= k:
                num -= k
                res += v
        return res
