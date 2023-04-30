class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        """收集足够苹果的最小花园周长
        1. dp, 时间复杂度O(n)
        单串, 位置i必取, O(1)个子问题
        i = 1, 3*3-1 个点
        i = 2, 5*5-1 个点
        i = 3, 2*3+1 个点
        dp[i] = dp[i-1] + 4 *(i*(2*i+1) + i*(i+1)) - 2*i*4

        2. 二分, 时间复杂度O(logn)
        半径为i的正方形含有苹果数量:
        (2i+1)*(1+2+...+i)*2*2 = (2i+1)*(i+1)*i*2
        """
        # # 1.
        # i = 1
        # cur = 0
        # while True:
        #     cur = cur + 4 *(i*(2*i+1) + i*(i+1)) - 2*i*4
        #     if cur >= neededApples:
        #         break
        #     i += 1
        # return 8 * i

        # 2.
        def check(x):
            ans = (2*x+1) * (x+1) * x * 2
            return ans < neededApples

        l, r = 1, 10**15
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return 8*l