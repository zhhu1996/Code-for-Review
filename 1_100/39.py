class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #         # 1. 暴力法
        #         self.res = set()

        #         def calcSum(candidate, now, nowSum, target):
        #             if nowSum > target:
        #                 return
        #             if nowSum == target:
        #                 self.res.add(tuple(sorted(now.copy())))
        #                 return
        #             for i in range(len(candidate)):
        #                 now.append(candidate[i])
        #                 calcSum(candidate, now, nowSum+candidate[i], target)
        #                 now.pop()

        #         calcSum(candidates, [], 0, target)
        #         return list(self.res)

        # 2. 回溯法 + 巧妙剪枝
        candidates.sort()
        self.res = []

        def calcSum(candidate, index, now, nowSum, target):
            if nowSum > target:
                return
            if nowSum == target:
                self.res.append(now.copy())
                return
            for j in range(index, len(candidate)):
                now.append(candidate[j])
                calcSum(candidate, j, now, nowSum + candidate[j], target)
                now.pop()

        calcSum(candidates, 0, [], 0, target)
        return self.res