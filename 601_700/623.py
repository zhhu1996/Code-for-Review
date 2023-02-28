# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """在二叉树中增加一行
        1. bfs
        2. dfs
        """
        # # 1.  
        # from queue import Queue
        # if depth == 1:
        #     new_root = TreeNode(val, root)
        #     return new_root
        # q = Queue(-1)
        # q.put(root)
        # cur_d = 1
        # while not q.empty() and cur_d < depth:
        #     size = q.qsize()
        #     for i in range(size):
        #         cur = q.get()
        #         if cur_d + 1 == depth:
        #             node1 = TreeNode(val)
        #             node1.left = cur.left
        #             cur.left = node1
        #             node2 = TreeNode(val)
        #             node2.right = cur.right
        #             cur.right = node2
        #         else:
        #             if cur.left:
        #                 q.put(cur.left)
        #             if cur.right:
        #                 q.put(cur.right)
        #     cur_d += 1
        # return root

        # 2.  
        def dfs(root, cur):
            if not root: return
            if cur + 1 == depth:
                node1 = TreeNode(val)
                node1.left = root.left
                root.left = node1
                node2 = TreeNode(val)
                node2.right = root.right 
                root.right = node2
            elif cur < depth:
                dfs(root.left, cur+1)
                dfs(root.right, cur+1)
            else:
                return
        
        if depth == 1:
            new_root = TreeNode(val, root)
            return new_root
        dfs(root, 1)
        return root