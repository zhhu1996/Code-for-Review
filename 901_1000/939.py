class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        """最小矩形面积
        1. 暴力, 时间复杂度O(n^3)
        用哈希表存储每个横坐标对应的点集, 然后遍历所有横坐标, 如果交集>2, 说明可以组成矩形

        2. 对角线, 时间复杂度O(n^2)
        枚举所有对角线组合, 判断是否能组成矩形
        """
        # # 1.
        # pdict = {}
        # for p in points:
        #     if p[0] in pdict:
        #         pdict[p[0]].add(p[1])
        #     else:
        #         pdict[p[0]] = set([p[1]])
        # key = list(sorted(pdict.keys()))
        # ans = float('inf')
        # for i in range(len(key)-1):
        #     for j in range(i+1, len(key)):
        #         s1, s2 = pdict[key[i]], pdict[key[j]]
        #         s = list(s1 & s2)
        #         if len(s) < 2:
        #             continue
        #         s.sort()
        #         for k in range(len(s)-1):
        #             ans = min(ans, (key[j]-key[i])*(s[k+1]-s[k]))
        # return ans if ans < float('inf') else 0


        # 2.
        mset = set()
        for p in points:
            mset.add(tuple(p))
        n = len(points)
        ans = float('inf')
        for i in range(n-1):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2 and (x1, y2) in mset and (x2, y1) in mset:
                    ans = min(ans, abs(x1-x2)*abs(y1-y2))
        return ans if ans < float('inf') else 0