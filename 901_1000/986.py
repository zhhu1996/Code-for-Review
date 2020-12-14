class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """区间列表的交集
        1. 双指针
        i指向A的第一个元素，j指向B的第一个元素，由于A，B的内部都不可能找不到交集，交集只可能发生在A、B之间
        通过比较A[i][-1]与B[j][-1]的大小来确定哪个指针移动
        在移动指针的同时，需要判断A的左区间与B的有区间是否相交，相交则加入结果集
        """
        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i][-1] < B[j][-1]:
                if A[i][-1] >= B[j][0]:
                    temp = [max(A[i][0], B[j][0]), A[i][-1]]
                    result.append(temp)
                i += 1
            elif A[i][-1] > B[j][-1]:
                if B[j][-1] >= A[i][0]:
                    temp = [max(A[i][0], B[j][0]), B[j][-1]]
                    result.append(temp)
                j += 1
            else:
                temp = [max(A[i][0], B[j][0]), B[j][-1]]
                result.append(temp)
                j += 1
                i += 1
        return result
