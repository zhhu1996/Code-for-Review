class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        """k个空花盆
        1. 暴力解法，对于当前元素j，判断visited[j-K-1]==1 and sum(visited[j-K:j])==0是否满足；或者visited[j+K+1]==1 and sum(visited[j+1: j+K+1])是否满足
            时间复杂度O(N*K)，N是花的个数，K是输入
        2. 滑动窗口法，用一个数组days记录每盆花开放的日期，设置两个指针left和right，循环结束条件是right小于花盆个数。
        首先窗口的初始值是：left从0开始，right从0+K+1开始，
        检查days，中间的数是否都小于left和right，如果都小于，我们就找到了一个候选结果（left和right中的较大值）更新left =right, right = right+K+1
        如果在位置i，days[i]小于左右两边中的一个数，那么我们更新left = i, right = i+K+1
        取满足条件的结果中最小的一个就是题目答案，
        时间复杂度O(N)，每个元素只会被比较一次
        """
        # n = len(bulbs)
        # visited = [0] * n # 0表示不开
        # for i in range(n):
        #     j = bulbs[i]-1
        #     visited[j] = 1
        #     if j+K+1 < n and visited[j+K+1] and sum(visited[j+1:j+K+1])==0:
        #         return i+1
        #     if j-K-1 >= 0 and visited[j-K-1] and sum(visited[j-K:j])==0:
        #         return i+1
        # return -1

        n = len(bulbs)
        days = [float("inf")]*n
        for i in range(n):
            j = bulbs[i]-1
            days[j] = i+1
        left, right, result = 0, K+1, float("inf")
        while right < n:
            flag = True
            for j in range(left+1, right):
                if days[j] <= days[left] or days[j] <= days[right]:
                    left = j
                    right = j+K+1
                    flag = False
                    break
            if flag:
                result = min(result, max(days[left], days[right]))
                left = right
                right = right + K + 1
        if result == float("inf"):
            return -1
        return result

