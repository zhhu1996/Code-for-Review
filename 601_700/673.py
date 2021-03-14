class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        依赖比i小的O(i)个子问题
        length[i]表示以nums[i]结尾的LIS的长度
        count[i]表示以nums[i]结尾的LIS的组合数

        length[i]与LIS长度的解题思路相同
        count[i]的求解方式为
        在nums[i] > nums[j]的前提下
        if length[j] + 1 > length[i]，表示遇到新的组合使长度更大，
            length[i] = length[j]+1
            count[i] = count[j]
        elif 相等, 表示并未遇到新组合使长度更大,
            count[i] += count[j]

        最后统计所有等于最大长度的count
        """
        if not nums:
            return 0

        n = len(nums)
        length = [1] * n
        count = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        maxlen = max(length)
        result = 0
        for i in range(n):
            if length[i] == maxlen:
                result += count[i]
        return result


