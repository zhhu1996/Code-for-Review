class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        """最小公共区域
        1. 先建树, 再根据region1, region2计算出到根节点的路径
        """
        tree = {}
        for region_list in regions:
            for i in range(1, len(region_list)):
                tree[region_list[i]] = region_list[0]
        
        def find_path(tree, key):
            node = key
            path = []
            while node in tree:
                path.append(node)
                node = tree[node]
            path.append(node) # root
            return path

        p1 = find_path(tree, region1)
        p2 = find_path(tree, region2)
        len1, len2 = len(p1), len(p2)
        i = 1
        while len1-i>=0 and len2-i>=0 and p1[len1-i] == p2[len2-i]:
            i += 1
        return p1[len1-i+1]
        