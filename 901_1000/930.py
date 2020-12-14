import collections

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        """和相同的二元子数组
        1. 枚举所有子数组，时间复杂度O(n2)

        2. 前缀和 + 哈希表搜索
        """
        # n = len(A)
        # result = 0
        # for i in range(n):
        #     cumsum = 0
        #     for j in range(i, n):
        #         cumsum += A[j]
        #         if cumsum == S:
        #             result += 1
        # return result

        P = [0]
        for x in A:
            P.append(P[-1] + x)
        count = collections.defaultdict(int)

        ans = 0
        for x in P:
            ans += count[x]
            count[x + S] += 1

        return ans
