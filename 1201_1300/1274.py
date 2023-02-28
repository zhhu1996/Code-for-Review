# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        """矩形内船只的数目
        1. 暴力
        i. 1000*1000个点都搜索一遍, 时间复杂度O(n^2)
        ii. 先搜1000列, 再搜1000行, 时间复杂度O(n)
        优化: 分治法求4个小矩形的船只, 再汇总
        2. 二分
        通过二分搜索满足条件的行, 再二分搜索对应的列
        """

        start_x, end_x = bottomLeft.x, topRight.x
        start_y, end_y = bottomLeft.y, topRight.y
        res = 0
        used = 0
        while start_x <= end_x: # 搜索行
            l, r = start_x, end_x
            while l <= r:
                mid = (l + r) // 2
                # f(l-1) = False, f(r+1) = True
                if sea.hasShips(Point(mid, end_y), Point(start_x, 0)):
                    r = mid - 1
                else:
                    l = mid + 1
                used += 1
            # l即为第一个True
            if l <= end_x: # 搜索列
                row = l
                y3, y4 = bottomLeft.y, topRight.y
                while y3 <= y4:
                    lo, hi = y3, y4
                    while lo <= hi:
                        mid = (lo + hi) // 2
                        # f(lo-1) = False, f(hi+1) = True
                        if sea.hasShips(Point(row, mid), Point(row, y3)):
                            hi = mid - 1
                        else:
                            lo = mid + 1
                        used += 1
                    # lo即为第一个True
                    if lo <= y4:
                        res += 1
                        y3 = lo + 1
                    else:
                        break
                start_x = row + 1
            else:
                break
        print(used)
        return res