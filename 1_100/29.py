class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 1. 对除数做减法
        # => 优化: 每次对被除数乘2, 再对除数做减法
        flag = 0
        if dividend < 0: 
            flag += 1
            dividend = -dividend
        if divisor < 0: 
            flag += 1
            divisor = -divisor 

        def simple_calc_div(x, y):
            cnt = 0
            while x >= y:
                cnt += 1
                x -= y
            return cnt

        def binary_calc_div(x, y):
            if x < y:
                return 0
            cnt, base = 1, y
            while y+y <= x:
                cnt = cnt+cnt
                y = y+y
            return cnt + binary_calc_div(x-y, base)

        res = (-1)**flag *binary_calc_div(dividend, divisor)
        if res < -2**31: res = -2**31
        if res > 2**31-1: res = 2**31-1
        return res