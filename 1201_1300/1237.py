"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        # x,y的值域为[1,1000], 遍历x, 通过二分法寻找y使得f(x, y)=z
        res= []
        for x in range(1,1001):
            # 寻找y使得f(x,y)=z
            left, right = 1, 1000
            while left < right:
                mid = (left+right) // 2
                if customfunction.f(x, mid) < z:
                    left = mid+1
                else:
                    right = mid
            if customfunction.f(x, left) == z:
                res.append([x, left])
        return res 