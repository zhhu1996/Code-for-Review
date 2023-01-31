class Solution:
    def countAndSay(self, n: int) -> str:
        # # 1. 暴力遍历
        # if n <= 1: return '1'
        # res = ['1']
        # for i in range(n-1):
        #     target = res[-1]
        #     temp = ''
        #     j = 0
        #     while j < len(target):
        #         cnt = 1
        #         base = target[j]
        #         while j < len(target)-1 and target[j] == target[j+1]:
        #             j += 1
        #             cnt += 1
        #         temp += str(cnt) + base
        #         j += 1
        #     res.append(temp)
        # return res[-1]
            
        # 2. 双指针优化版本
        if n <= 1: return '1'
        target = '1'
        for i in range(n-1):
            temp = ''
            start, end = 0, 0
            while end < len(target):
                cnt = 0
                while end < len(target) and target[end] == target[start]:
                    end += 1
                    cnt += 1
                temp += str(cnt) + target[start]
                start = end
            target = temp
        return target