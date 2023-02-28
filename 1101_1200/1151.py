class Solution:
    def minSwaps(self, data: List[int]) -> int:
        """最少交换次数来组合所有的1
        1. 定长滑动窗口
        窗口长度k=所有1的个数
        """
        n = len(data)
        k = sum(data)
        cur = sum(data[:k])
        res = k-cur
        for i in range(k, n):
            if data[i] == 1:
                cur += 1
            if data[i-k] == 1:
                cur -= 1
            res = min(res, k-cur)
        return res