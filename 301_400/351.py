class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        """安卓系统手势解锁
        1. 回溯
        解锁手势总和 = 经过的点在[m,n]之间的加和
        """