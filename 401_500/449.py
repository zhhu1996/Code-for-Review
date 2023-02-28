# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """序列化和反序列化二叉搜索树
    1. 不考虑BST的性质, 当成普通二叉树求解

    2. 序列化时按照前序遍历, 反序列化时根据root节点可以区分左子树和右子树
    """
    def serialize(self, root):
        """Encodes a tree to a single string.
    
        :type root: TreeNode
        :rtype: str
        """
        if not root: return 'null'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + ',' + left + ',' + right


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        s = data.split(',')

        def build_tree(slist):
            val = slist.pop(0)
            if val == 'null':
                return None
            root = TreeNode(val)
            root.left = build_tree(slist)
            root.right = build_tree(slist)
            return root

        return build_tree(s)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans