class Solution:
    def isValid(self, s: str) -> bool:
        # 用堆栈来实现括号匹配
        # 左括号则压入堆栈，右括号则跟栈顶元素匹配，不匹配代表不满足条件
        # 最后字符串输完，如果堆栈中还有元素，说明未完成匹配
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif c == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif c == ']' and stack and stack[-1] == '[':
                stack.pop()
            else:
                return False

        return not stack