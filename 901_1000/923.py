from collections import Counter
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        """三数之和的多种可能
        双指针，计算所有满足的组合（单纯的双指针超时）
        需要记录相等的元素个数
        """
        cnt = 0
        n = len(A)
        A.sort()
        right = [0 for i in range(n)]
        right[-1] = 1
        for i in range(n-2, -1, -1):
            if A[i] == A[i+1]:
                right[i] = right[i+1] + 1
            else:
                right[i] = 1
        left = [0 for i in range(n)]
        left[0] = 1
        for i in range(1, n):
            if A[i] == A[i-1]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 1
        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                now = A[i] + A[j] + A[k]
                if now < target:
                    j += 1
                elif now > target:
                    k -= 1
                elif A[j] != A[k]:
                    # cntJ = 1
                    # while j < k and A[j] == A[j+1]:
                    #     cntJ += 1
                    #     j += 1
                    # j += 1
                    # cntK = 1
                    # while k > j and A[k] == A[k-1]:
                    #     cntK += 1
                    #     k -= 1
                    # k -= 1
                    # cnt += cntJ * cntK
                    cnt += right[j] * left[k]
                    j += right[j]
                    k -= left[k]
                else: # A[j] == A[k]
                    m = k - j + 1
                    cnt += m*(m-1)//2
                    break
        return cnt % (10**9 + 7)