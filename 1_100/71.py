# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.parent = None

class Solution:
    def simplifyPath(self, path: str) -> str:
        # # 1. 直接调用库函数
        # import os.path
        # return os.path.abspath(path)

        # 2. 首先将路径分隔开，遇到.则跳过，遇到..则弹出堆栈内的元素，否则压入堆栈新元素
        p = [i for i in path.split('/') if i]
        stack = []
        for c in p:
            if c == '.':
                continue
            elif c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return '/' + '/'.join(stack)