# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        """序列化二叉树
        1. 构建前序和中序遍历的序列，反序列化成一颗二叉树（缺点：需要读取完全部数据才能反序列化）
        2. 只根据前序遍历的序列实时反序列化（优点：动态解析）
        """
        self.index = 0

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "$"
        result = [root.val]
        result.extend(self.serialize(root.left))
        result.extend(self.serialize(root.right))
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if self.index >= len(data):
            return
        if data[self.index] == '$':
            self.index += 1
            return None
        root = TreeNode(data[self.index])
        self.index += 1
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
