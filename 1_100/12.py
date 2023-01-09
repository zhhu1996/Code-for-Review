class Solution:
    def intToRoman(self, num: int) -> str:
        # # 1. 暴力匹配
        # def transfer_one_digit(num, base, chars):
        #     # chars = ['I', 'V', 'X'], 从小到大排列
        #     s = ''
        #     if num // base == 4:
        #         s += chars[0] + chars[1]
        #     elif num // base == 9:
        #         s += chars[0] + chars[-1]
        #     elif num // base < 5:
        #         s += chars[0] * (num // base)
        #     elif num // base >= 5:
        #         s += chars[1] + chars[0]*(num%(5*base)//base)
        #     return s
        # res = ''
        # if num >= 1000:
        #     res += 'M' * (num//1000)
        #     num = num % 1000
        # res += transfer_one_digit(num, 100, ['C', 'D', 'M'])
        # res += transfer_one_digit(num%100, 10, ['X', 'L', 'C'])
        # res += transfer_one_digit(num%10, 1, ['I', 'V', 'X'])
        # return res

        # 2. 基于贪心的思想，每次拿最大值去匹配～
        res = ''
        dic = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
               4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        for k, v in sorted(dic.items(), key=lambda x: x[0], reverse=True):
            while num >= k:
                num -= k
                res += v
        return res
