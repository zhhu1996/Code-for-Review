class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 1. 回溯法
        self.res = []
        if len(s) > 12:
            return []

        self.hs(s, [], 0)
        return self.res

    def hs(self, s, ns, index):
        if index >= len(s):
            if index == len(s) and len(ns) == 4:
                self.res.append('.'.join(ns.copy()))
            return

        for i in range(1, 4):
            if self.judge(s[index: index + i]):
                ns.append(s[index: index + i])
                self.hs(s, ns, index + i)
                ns.pop()

    def judge(self, num):
        if int(num) <= 255 and str(int(num)) == num:
            return True

        return False