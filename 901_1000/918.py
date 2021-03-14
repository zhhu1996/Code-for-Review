class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        """环形子数组的最大和
        dp[i]表示以i结尾的子数组的最大和
        dp[i]的求解需要分情况讨论:
        i. 单区间
        即求a[:i]的子数组最大和
        ii. 双区间
        令R[j] = a[j] + a[j+1] + ... + a[-1]
        则dp[i] = a[0] + a[1] + ... + a[i] + max(R[j]), j >= i+2
        """

        # 单区间求解
        cur,ans = A[0],A[0]
        n = len(A)
        for i in range(1,n):
            cur = A[i] + max(cur,0)
            ans = max(cur,ans)

        # 双区间求解
        rightSum = [0] * n
        rightSum[-1] = A[-1]
        for i in range(n-2,-1,-1):
            rightSum[i] = rightSum[i+1] + A[i]

        maxRight = [0] * n
        maxRight[-1] = A[-1]
        for i in range(n-2,-1,-1):
            maxRight[i] = max(maxRight[i+1],rightSum[i])

        leftSum = 0
        for i in range(n-2):
            leftSum += A[i]
            ans = max(ans, leftSum+maxRight[i+2])
        return ans