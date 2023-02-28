# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """二叉树的垂直遍历
        1. 层序遍历
        队列中存放节点值与对应的输出序, 在遍历时保存每个输出序内的元素顺序, 最后再排序输出
        """
        from queue import Queue
        if not root: return []
        lvs = {}
        q = Queue(-1)
        q.put((root, 0)) # (node, lv)
        while not q.empty():
            node, lv = q.get()
            if lv in lvs:
                lvs[lv].append(node.val)
            else:
                lvs[lv] = [node.val]
            if node.left:
                q.put((node.left, lv-1))
            if node.right:
                q.put((node.right, lv+1))
        res = []
        for k, v in sorted(lvs.items(), key=lambda x: x[0], reverse=False):
            res.append(v)
        return res