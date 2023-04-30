class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """区间列表的交集
        1. 双指针
        i指向A的第一个元素，j指向B的第一个元素，由于A，B的内部都不可能找不到交集，交集只可能发生在A、B之间
        通过比较A[i][-1]与B[j][-1]的大小来确定哪个指针移动
        在移动指针的同时，需要判断A的左区间与B的有区间是否相交，相交则加入结果集
        """
        i, j = 0, 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                ans.append([start, end])
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1
        return ans