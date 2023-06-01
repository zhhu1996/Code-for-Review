class Solution:
    def minInsertions(self, s: str) -> int:
        """平衡括号字符串的最少插入次数
        1. 遍历 + 堆栈
        s[i] = '(' -> 入栈
        s[i] = ')' -> 
            s[i+1] = ')': 出栈
            s[i+1] = '(': 插入')'或'('
        最后根据堆栈剩余的'('梭哈计算需要插入的字符数
        """
        n = len(s)
        stk = []
        i = 0
        ans = 0
        while i < n:
            if s[i] == '(':
                stk.append(s[i])
                i += 1
            else:
                if stk:
                    stk.pop()
                else:
                    ans += 1
                if i+1 < n and s[i+1] == ')':
                    i += 2
                else:
                    ans += 1
                    i += 1
        ans += len(stk)*2
        return ans