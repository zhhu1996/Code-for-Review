class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        """健身计划评估
        1. 滑动窗口
        每次维护一个k大小的窗口，并计算窗口的总和，与lower、uppper进行比较
        """
        i, j = 0, 0
        n = len(calories)
        windowSum = 0
        result = 0
        totalSum = sum(calories[i: k])
        for j in range(k-1, n):
            # totalSum = sum(calories[i: j+1])
            if j > k-1:
                totalSum += calories[j]
            if totalSum < lower:
                result -= 1
            elif totalSum > upper:
                result += 1
            totalSum -= calories[i]
            i += 1
        return result




