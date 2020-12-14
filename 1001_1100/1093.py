class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        """大样本统计
        在遍历一遍的时候维护局部最大值和局部最小值，可得到全局的最大最小值；
        同时维护一个局部计数变量的全局计数变量来计算众数；
        用双指针求中位数和平均数
        中位数就是双指针的平均值
        平均数需要记录所有元素的和以及元素个数，注意每次比较必定移动一个指针，否则会超时
        算法时间复杂度O(n)，n=256
        """
        globalMin, globalMax = float("inf"), 0
        maxCount, maxCountNum = 0, 0
        totalCnt, totalSum = 0, 0
        i, j = 0, 255
        while i < j:
            if count[i] == 0 and count[j] == 0:
                i += 1
                j -= 1
            elif count[i] == 0:
                i += 1
            elif count[j] == 0:
                j -= 1
            else:  # 都非0
                globalMin = min(globalMin, i)
                globalMax = max(globalMax, j)
                if maxCount < count[i]:
                    maxCount = count[i]
                    maxCountNum = i
                if maxCount < count[j]:
                    maxCount = count[j]
                    maxCountNum = j
                if count[i] > count[j]:
                    minIndex, maxIndex = j, i
                else:
                    minIndex, maxIndex = i, j
                totalSum += count[minIndex] * minIndex
                totalCnt += count[minIndex]
                totalSum += count[minIndex] * maxIndex
                totalCnt += count[minIndex]
                count[maxIndex] = count[maxIndex] - count[minIndex]
                count[minIndex] = 0
        if i == j:
            totalCnt += count[i]
            totalSum += i * count[i]
        return [globalMin, globalMax, totalSum / totalCnt, (i + j) / 2, maxCountNum]
