class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """和为s的连续正数序列
        两个指针，一个指向窗口的最小值，一个指向窗口的最大值，根据当前窗口内元素的和与target之间的关系来调整两个指针
        if curSum > target, small += 1
        if curSum < target, big += 1
        """
        if target < 3:
            return []
        small, big = 1, 2
        nowSum = small + big
        result = []

        def getResult(index1, index2):
            return [i for i in range(index1, index2+1)]

        while small <= target // 2:
            if nowSum < target:
                big += 1
                nowSum += big
            else:
                if nowSum == target:
                    result.append(getResult(small, big))
                nowSum -= small
                small += 1
        return result



