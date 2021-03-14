class NumArray:
    """
    方法1: 暴力法，时间复杂度O(n^2)

    方法2: 前缀和
    sum(i,j) = T(j)-T(i-1)
    T(j)表示数组[0,j]的和
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dp = []
        self.calDP()

    def calDP(self):
        # # 方法1
        # n = len(self.nums)
        # for i in range(n):
        #     cur = 0
        #     temp = [0 for i in range(n)]
        #     for j in range(i, n):
        #         cur += self.nums[j]
        #         temp[j] = cur
        #     self.dp.append(temp)

        # 方法2
        cur = 0
        for i in range(len(self.nums)):
            cur += self.nums[i]
            self.dp.append(cur)

    def sumRange(self, i: int, j: int) -> int:
        if i >= 1:
            return self.dp[j] - self.dp[i-1]
        else:
            return self.dp[j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)