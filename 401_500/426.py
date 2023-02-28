"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.sort_arr = []

        def dfs(root):
            if not root: return
            dfs(root.left)
            self.sort_arr.append(root)
            dfs(root.right)
        
        if not root:
            return root
        dfs(root)
        n = len(self.sort_arr)
        for i in range(n):
            self.sort_arr[i].left = self.sort_arr[(i-1+n) % n]
            self.sort_arr[i].right = self.sort_arr[(i+1+n) % n]
        return self.sort_arr[0]
