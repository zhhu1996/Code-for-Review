# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue

class Codec:
    """二叉树的序列化与反序列化
    1. BFS
    2. DFS(前序/后序)
    """

    # 1. BFS
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        q = Queue(-1)
        q.put(root)
        enc = []
        while not q.empty():
            it = q.get()
            if it:
                enc.append(str(it.val))
                q.put(it.left)
                q.put(it.right)
            else:
                enc.append('null')
        return ','.join(enc)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        s = data.split(',')
        q = Queue(-1)
        root = TreeNode(s[0])
        q.put(root)
        index = 1
        while not q.empty():
            node = q.get()
            if index < len(s) and s[index] != 'null':
                node.left = TreeNode(s[index])
                q.put(node.left)
            if index+1 < len(s) and s[index+1] != 'null':
                node.right = TreeNode(s[index+1])
                q.put(node.right)
            index += 2 
        return root

    # 2. DFS
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
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))