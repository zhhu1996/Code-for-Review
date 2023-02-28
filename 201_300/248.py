class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        """中心对称数III
        满足条件的组合: (6,9),(9,6),(0,0),(1,1),(8,8)
        举例:
            0-9: 0,1,8
            10-99: 11, 88, 69, 96
            100-999: 101,181,111,808,888,818,609,689,619,906,916,986
        回溯生成所有的中心对称数, 再选取区间内的作为结果返回
        """
        self.cnt = 0
        self.candidate = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        
        def compare(s1, s2):
            # to judge s1 > s2
            if len(s1) == len(s2):
                for i in range(len(s1)):
                    if int(s1[i]) > int(s2[i]):
                        return True
                    elif int(s1[i]) < int(s2[i]):
                        return False
                    else:
                        continue
                return True
            return len(s1) > len(s2)

        def gen_slist(sl, left, right):
            """
            sl: 生成序列
            left: 左指针
            right: 右指针
            """
            if left > right:
                if len(sl) == 1 or sl[0] != '0':
                    if compare(sl, list(low)) and compare(list(high), sl):
                        self.cnt += 1
                return
            for k, v in self.candidate.items():
                if left == right and k != v:
                    continue
                sl[left] = k
                sl[right] = v
                gen_slist(sl, left+1, right-1)

        for target in range(len(low), len(high)+1):
            s = ['0']*target
            gen_slist(s, 0, target-1)    
        return self.cnt     