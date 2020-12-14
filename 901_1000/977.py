class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        """有序数组的平方
        1. 双指针，先找到第一个大于0的数字，索引记为split，如果是数组的第一个数字，那么直接返回平方数组；
        否则i指向split-1，j指向第一个大于0的数字，比较平方和
        """
        n = len(A)
        split = n
        for i in range(len(A)):
            if A[i] >= 0:
                split = i
                break
        if split == 0: # 全是+
            return [x*x for x in A]
        elif split == n: # 全是-
            return [A[i]*A[i] for i in range(len(A)-1, -1, -1)]
        else: # +,-
            i, j = split-1, split
            result = []
            while i >= 0 and j < n:
                num1 = A[i]*A[i]
                num2 = A[j]*A[j]
                if num1 <= num2:
                    result.append(num1)
                    i -= 1
                else:
                    result.append(num2)
                    j += 1
            while i >= 0:
                result.append(A[i]*A[i])
                i -= 1
            while j < n:
                result.append(A[j]*A[j])
                j += 1
            return result


