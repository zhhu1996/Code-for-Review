class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        """将数组拆分成斐波那契序列
        1. 回溯 + 剪枝, 时间复杂度O(n*logC*logC), C=2**31
        """
        def gen_cand(index, path):
            if index == len(num):
                if len(path) >= 3:
                    self.ans = path.copy()
                return
            for i in range(index, len(num)):
                if int(num[index: i+1]) >= 2**31:
                    return
                if num[index] == '0' and i > index:
                    return
                if len(path) >= 2 and int(num[index: i+1]) != path[-1] + path[-2]:
                    continue
                path.append(int(num[index: i+1]))
                gen_cand(i+1, path)
                path.pop()
        
        self.ans = []
        gen_cand(0, [])
        return self.ans