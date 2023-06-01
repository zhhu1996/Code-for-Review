class Solution:
    def isHappy(self, n: int) -> bool:
        """快乐数
        1. 枚举
        n的取值范围决定了最大平方和为1+81*9=730, 因此730次循环之内必出现重复

        2. 快慢指针
        """
        # # 1.
        # cnt = 0
        # while n != 1 and cnt < 10**3:
        #     cur = 0
        #     while n > 0:
        #         cur += (n%10) * (n%10)
        #         n = n // 10
        #     cnt += 1
        #     n = cur
        # return True if n == 1 else False

        # 2.
        def calc_square(num):
            ans = 0
            while num > 0:
                ans += (num % 10) * (num % 10)
                num = num // 10
            return ans
        
        slow, fast = n, n
        while True:
            slow = calc_square(slow)
            fast = calc_square(fast)
            fast = calc_square(fast)
            if slow == fast:
                break
        return slow == 1