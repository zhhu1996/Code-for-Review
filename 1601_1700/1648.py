class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        """销售价值减少的颜色球
        1. 贪心 + 二分
        i) 先对价值排序, 每次取最大价值的球
        ii)构造函数f(x), x的定义域为[0, n-1], 满足二分性 
        """
        n = len(inventory)
        inventory.sort(reverse=True)

        def calc_val(x):
            ans = 0
            target = x
            for i in range(len(inventory)):
                if inventory[i] < x:
                    break
                ans += (inventory[i] + target) * (inventory[i] - target + 1) // 2
            return ans

        def calc_cnt(x):    
            ans = 0
            for i in range(len(inventory)):
                if inventory[i] < x:
                    break
                ans += (inventory[i]-x+1)
            return ans

        def check(x):
            return calc_cnt(x) < orders

        l, r = 1, max(inventory)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        # f(l-1) >= orders, f(l) < orders
        cnt0 = calc_cnt(l)
        val0 = calc_val(l)
        return (val0 + (orders-cnt0)*(l-1)) % (10**9 + 7)