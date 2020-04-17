# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(start, end):
            if start > end:
                return [None]

            all_trees = []
            for i in range(start, end + 1):
                root = i
                tree_left = generate(start, i - 1)
                tree_right = generate(i + 1, end)
                for l in tree_left:
                    for r in tree_right:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        all_trees.append(cur)
            return all_trees

        return generate(1, n) if n else []