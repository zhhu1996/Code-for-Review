class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        """
        # 1. 构建二维dp数组，dp[i][j]等于A[i:j]的最小值，dp[i][j] = min(dp[i][j-1], A[j])， 超时
        # 2. 计算每个元素作为最小值的子数组个数，设置两个数组left, right
        left[i]表示在数组A中，index<i && A[index] < A[i]的第一个元素的索引
        right[i]表示在数组A中，index>i && A[index] < A[i]的第一个元素的索引
        因此对于数组中的每一个元素A[i]
        可形成的最小子数组个数为(i - left[i]) * (right[i] - i)
        则总和为sum((i - left[i]) * (right[i] - i))

        接下来的问题就是如何求解left数组和right数组：
        暴力解的话就每一步都遍历A[i]左边的元素和右边的元素，时间复杂度为O(n^2)
        巧妙的方法是使用堆栈快速求解：
        对于left数组，从左到右遍历入栈，栈中只保留比当前元素小的元素的索引，证明如下
        假设A[i] > A[i+1]，那么比A[i]大的元素肯定也大于A[i+1]，不可能是满足条件的元素；
        假设A[i] < A[i+1]，那么left[i+1]直接等于i，不需要再查找了；
        (栈空的情况下，直接等于-1)
        对于right数组，从右到左遍历入栈，栈中只保留比当前元素小的元素的索引，证明同上
        假设A[i] > A[i+1]，那么right[i]直接等于i+1，不需要再查找了；
        假设A[i] < A[i+1]，那么比A[i+1]大的元素肯定也大于A[i]，没有查找的必要；
        (栈空的情况下，直接等于len(A))
        """
        if not A:
            return 0

        lenA = len(A)
        stack = []
        left, right = [0]*(lenA), [0]*(lenA)
        for i in range(len(A)):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            if not stack:
                left[i] = -1
            else:
                left[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(len(A)-1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            if not stack:
                right[i] = len(A)
            else:
                right[i] = stack[-1]
            stack.append(i)
        result = 0
        for i in range(len(A)):
            result += (i-left[i]) * (right[i]-i) * A[i]
        return result % (10**9 + 7)
