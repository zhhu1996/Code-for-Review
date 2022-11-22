class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in ["+", "-", "*", "/"]:
                temp1 = int(stack.pop())
                temp2 = int(stack.pop())
                result = 0
                if c == "+":
                    result = temp1 + temp2
                elif c == "-":
                    result = temp2 - temp1
                elif c == "*":
                    result = temp2 * temp1
                else:
                    result = int(temp2 / temp1)
                stack.append(result)
            else:
                stack.append(c)
        return int(stack.pop())
