class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. 去重可以采用对list排序后存入set，也可以手动判断
        candidates.sort()
        self.res = []

        def calcSum(candidate, index, now, nowSum, target):
            if nowSum > target:
                return
            if nowSum == target:
                self.res.append(now.copy())
                return
            for j in range(index, len(candidate)):
                if j > index and candidate[j] == candidate[j-1]:
                    """这个方法最重要的作用是，可以让同一层级，不出现相同的元素。假设candidates=【1，2，2，5】，即
                              1
                             / \
                    例1：    2   2  这种情况不会发生 
                           /     \
                          5       5
                    
                              1
                             /
                    例2：    2      这种情况确是允许的
                           /
                          2       
                    为何会有这种神奇的效果呢？
                    首先 candidate[cur-1] == candidate[cur] 是用于判定当前元素是否和之前元素相同的语句。这个语句就能砍掉例1。
                    可是问题来了，如果把所有当前与之前一个元素相同的都砍掉，那么例二的情况也会消失。 
                    因为当第二个2出现的时候，他就和前一个2相同了。
                                    
                    那么如何保留例2呢？
                    那么就用cur > begin 来避免这种情况，你发现例1中的两个2是处在同一个层级上的，
                    例2的两个2是处在不同层级上的。
                    在一个for循环中，所有被遍历到的数都是属于一个层级的。我们要让一个层级中，
                    必须出现且只出现一个2，那么就放过第一个出现重复的2，但不放过后面出现的2。
                    第一个出现的2的特点就是 cur == begin. 第二个出现的2 特点是cur > begin."""
                    continue
                now.append(candidate[j])
                calcSum(candidate, j+1, now, nowSum + candidate[j], target)
                now.pop()

        calcSum(candidates, 0, [], 0, target)
        return self.res