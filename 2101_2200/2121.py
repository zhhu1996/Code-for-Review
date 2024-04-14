class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        """相同元素的间隔之和
        1. 前缀和
        f[i] = base - (v[i]-v[0])*(n-i*2) - cumsum*2

        2. dp
        f[i] = f[i-1] + i*(v[i]-v[i-1]) - (n-i)*(v[i]-v[i-1])
        """
        # # 1.
        # kv = {}
        # for i, v in enumerate(arr):
        #     if v in kv:
        #         kv[v].append(i)
        #     else:
        #         kv[v] = [i]
        # ans = [0]*len(arr)
        # for k, v in kv.items():
        #     base = 0
        #     for i in range(1, len(v)):
        #         base += abs(v[0] - v[i])
        #     cumsum = 0
        #     for i in range(len(v)):
        #         if i == 0:
        #             ans[v[i]] = base
        #         else:
        #             cumsum += abs(v[i-1]-v[0])
        #             ans[v[i]] = base - (v[i]-v[0])*(len(v)-i*2) - cumsum*2
        # return ans


        # 2.
        kv = {}
        for i, v in enumerate(arr):
            if v in kv:
                kv[v].append(i)
            else:
                kv[v] = [i]
        ans = [0]*len(arr)
        for k, v in kv.items():
            base = 0
            for i in range(1, len(v)):
                base += abs(v[0] - v[i])
            for i in range(len(v)):
                if i == 0:
                    ans[v[i]] = base
                else:
                    ans[v[i]] = ans[v[i-1]] + i*(v[i]-v[i-1]) - (len(v)-i)*(v[i]-v[i-1])
        return ans