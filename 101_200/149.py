class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """直线上最多的点
        1. 暴力, 时间复杂度O(n^3)
        枚举所有斜率, 再统计其他点共线的个数
        2. 
        枚举所有起点, 再统计相等斜率的点个数(同起点相同斜率 => 共线)
        """
        # # 1.
        # n = len(points)
        # res = 1
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         a = points[i]
        #         b = points[j]
        #         cnt = 2
        #         for k in range(n):
        #             if k == i or k == j:
        #                 continue
        #             c = points[k]
        #             s1 = (c[1] - a[1]) * (b[0] - a[0])
        #             s2 = (c[0] - a[0]) * (b[1] - a[1])
        #             if s1 == s2:
        #                 cnt +=1
        #         res = max(res, cnt)
        # return res

        # 2.
        def gcd(y, x):
            # 求y, x的最大公因子
            return y if x == 0 else gcd(x, y%x)

        n = len(points)
        res = 1
        for i in range(n):
            kmap = {}
            for j in range(n):
                if j == i: continue
                x1, y1, x2, y2 = points[i][0], points[i][1], points[j][0], points[j][1]
                dy = y2 - y1
                dx = x2 - x1
                common = gcd(dy, dx)
                dy = dy // common
                dx = dx // common
                key = str(dy) + '_' + str(dx)
                if key in kmap:
                    kmap[key] += 1
                else:
                    kmap[key] = 2
            cur = 1
            if kmap:
                cur = sorted(kmap.items(), key=lambda x: x[-1], reverse=True)[0][1]
            res = max(res, cur)
        return res
            


        """ # 我的代码
        n = len(points)
        ks = {}
        vet = {}
        # 垂直x轴
        for i in range(n):
            xi = points[i][0]
            yi = points[i][1]
            if xi in vet:
                vet[xi].add(yi)
            else:
                vet[xi] = set([yi])
        # 不垂直于x轴
        for i in range(n-1):
            for j in range(i+1, n):
                dy = points[i][1] - points[j][1]
                dx = points[i][0] - points[j][0]
                if dx == 0:
                    continue
                # y = ax+b
                a = dy / dx
                b = points[j][1] - a*points[j][0]
                key = str(a) + '_' + str(b)
                ks[key] = 0
        for uk in ks.keys():
            ab = uk.split('_')
            a = float(ab[0])
            b = float(ab[1])
            for i in range(n):
                xi, yi = points[i][0], points[i][1]
                if abs(yi - a*xi - b) < 0.1**10: # 近似判断浮点数相等
                    ks[uk] += 1
        # cmp
        vertical = 0
        for k in vet.keys():
            vertical = max(vertical, len(vet[k]))
        maxk = 0
        if len(ks) > 0:
            kitem = sorted(ks.items(), key=lambda x: x[-1], reverse=True)[0]
            maxk = kitem[1]
        return max(maxk, vertical)
        """