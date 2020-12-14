class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """划分为k个相等的子集
        1. 回溯遍历

        """
        if not nums or k < 0:
            return False
        localSum = 0
        n = len(nums)
        self.calSum = []
        self.visited = [0] * n
        for i in range(n):
            localSum += nums[i]
            self.calSum.append(localSum)
        target = localSum // k

        def getCandidate(array, index, nowSum, count, target):
            """
            :param array: 搜索的数组
            :param index: 开始搜索的索引位置
            :param nowSum: 当前的和
            :param count: 总共需找到count组结果
            :param target: 目标和
            :return:
            """
            if count == 0:
                return True
            if nowSum > target:
                return False
            flag = False
            for j in range(index, len(array)):
                if not self.visited[j] and array[j] + nowSum <= target:
                    self.visited[j] = 1
                    if array[j] + nowSum == target:
                        flag = getCandidate(array, 0, 0, count - 1, target)
                    else:
                        flag = getCandidate(array, j + 1, nowSum + array[j], count, target)
                    if flag:
                        return True
                    self.visited[j] = 0
            return False

        return getCandidate(nums, 0, 0, k, target)