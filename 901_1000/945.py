class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # 1. 暴力迭代法，超时
        # A.sort()
        # result = 0
        # setA = set()
        # i = 0
        # while i < len(A):
        #     if A[i] not in setA:
        #         setA.add(A[i])
        #         i += 1
        #     else:
        #         while A[i] in setA:
        #             A[i] += 1
        #             result += 1
        # return result

        # 2. 每次递增太耗费时间，直接求需要计算多少次，核心：将 P 增加到 X 并且将 Q 增加到 Y，与将 P 增加到 Y 并且将 Q 增加到 X 都需要进行 (X + Y) - (P + Q) 次操作
        count = [0] * 80001
        res = 0
        for x in A:
            count[x] += 1
        need = 0
        for i in range(80001):
            if count[i] >= 2:
                need += (count[i] - 1)
                res -= i * (count[i] - 1)
            elif count[i] == 0 and need > 0:
                need -= 1
                res += i

        return res

        # 3. 排序
        A.sort()
        A.append(100000)
        ans = taken = 0

        for i in range(1, len(A)):
            if A[i - 1] == A[i]:
                taken += 1
                ans -= A[i]
            else:
                give = min(taken, A[i] - A[i - 1] - 1)
                ans += give * (give + 1) // 2 + give * A[i - 1]
                taken -= give

        return ans

