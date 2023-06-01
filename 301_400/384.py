import numpy as np

class Solution:
    """打乱数组
    1. shuffle

    2. Fisher-Yates 洗牌算法
    """

    def __init__(self, nums: List[int]):
        self.inits = nums
        self.cur = np.array(nums)


    def reset(self) -> List[int]:
        return self.inits


    def shuffle(self) -> List[int]:
        np.random.shuffle(self.cur)
        return self.cur.tolist()


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()