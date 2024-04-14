from sortedcontainers import SortedSet
import heapq

class FoodRatings:
    """设计食物评分系统
    1. 有序集合, 时间复杂度O(nlogn)

    2. 懒删除堆, 时间复杂度O(nlogn)
    在求最大值的时候验证food与rating, 如果不一致说明是已经被更改过的case, 直接丢弃
    """
    ## 1. 
    # def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
    #     self.fs = defaultdict(list)
    #     self.rk = defaultdict(SortedSet)
    #     for f, c, r in zip(foods, cuisines, ratings):
    #         self.fs[f] = [c, r]
    #         self.rk[c].add((-r, f))

    # def changeRating(self, food: str, newRating: int) -> None: # O(logn)
    #     if food not in self.fs:
    #         return
    #     c, r = self.fs[food]
    #     self.fs[food][1] = newRating
    #     self.rk[c].remove((-r, food))
    #     self.rk[c].add((-newRating, food))

    # def highestRated(self, cuisine: str) -> str: # O(1)
    #     return self.rk[cuisine][0][1]

    ## 2.
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.fs = defaultdict(list)
        self.rk = defaultdict(list)
        for f, c, r in zip(foods, cuisines, ratings):
            self.fs[f] = [c, r]
            heapq.heappush(self.rk[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None: # O(logn)
        if food not in self.fs: return
        c, r = self.fs[food]
        self.fs[food][1] = newRating
        heapq.heappush(self.rk[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str: # O(k*logn)
        cand = self.rk[cuisine]
        while -cand[0][0] != self.fs[cand[0][1]][1]:
            heapq.heappop(cand)
        return cand[0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)