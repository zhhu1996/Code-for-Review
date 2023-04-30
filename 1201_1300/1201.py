class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """丑数III
        1. 容斥 + 二分查找, 时间复杂度O(log(na))
        f(x)表示<=x的丑数是否小于n个, 在定义域上满足二分性
        """
        def gcd(a, b): # Greatest Common Divisor
            return gcd(b, a%b) if b > 0 else a
        
        def lcm(a, b): # Leatest Common Multiple
            return (a*b) // gcd(a,b)

        def calc_cnt(x):
            return x//a + x//b + x//c - x//ab - x//ac - x//bc + x//abc

        def check(x):
            return calc_cnt(x) < n

        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(ab, c)
        l, r = 1, min(n*a, n*b, n*c)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l