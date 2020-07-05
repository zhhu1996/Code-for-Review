class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed and not popped:
            return True
        if not pushed or not popped:
            return False
        stack = []
        # start表示已被压栈的最后一个元素索引，end表示需要被压栈的元素的索引
        start, end = -1, 0
        i = 0
        while i < len(popped):
            # print(i, stack)
            if stack and popped[i] == stack[-1]:
                stack.pop()
                i += 1
            else:
                end = pushed.index(popped[i])
                if end <= start:
                    return False
                for j in range(start + 1, end + 1):
                    stack.append(pushed[j])
                start = end
        return not stack
