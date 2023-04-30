class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """移除无效的括号
        1. 堆栈
        括号匹配题
        """
        stack = []
        n = len(s)
        d_set = set()
        for i in range(n):
            if s[i] not in ['(', ')']:
                continue
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    d_set.add(i)
        d_set = d_set | set(stack)
        ans = []
        for i, c in enumerate(s):
            if i not in d_set:
                ans.append(c)
        return ''.join(ans)