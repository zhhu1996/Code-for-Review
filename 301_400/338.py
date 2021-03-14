class Solution:
    def countBits(self, num: int) -> List[int]:
        """动态规划
        举例
        1:  01      ->      1
        2:  10      ->      1
        3:  11      ->      2
        4:  100     ->      1
        5:  101     ->      2=num[4]+num[1]
        6:  110     ->      2=num[4]+num[2]
        7:  111     ->      3=num[4]+num[3]
        8:  1000    ->      1
        观察可得:
        1-4是第一组数据，5-8是第二组数据
        9-16是第三组数据
        dp[i] = dp[2 ** j] + dp[i - 2 ** j]
        时间复杂度O(n)
        """
        dp = [0 for i in range(num + 1)]
        if num >= 1:
            dp[1] = 1
        if num >= 2:
            dp[2] = 1
        i = 3
        j = 1
        while i <= num:
            if i == 2 ** (j + 1):
                dp[i] = 1
                j += 1
            else:
                dp[i] = dp[2 ** j] + dp[i - 2 ** j]
            i += 1
        return dp
