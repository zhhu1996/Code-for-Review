class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        """颜色交替的最短路径
        1. bfs
        以(node, color)作为已经访问过的节点, coolr为入边
        """
        from queue import Queue

        mat = [defaultdict(list), defaultdict(list)]
        for e in redEdges: # Red
            mat[0][e[0]].append(e[1])
        for e in blueEdges: # Blue
            mat[1][e[0]].append(e[1])
        q = Queue(-1)
        ans = [-1]*n
        visit = set()
        q.put((0,0)) # (i, color)
        q.put((0,1))
        lv = 0
        while not q.empty():
            for i in range(q.qsize()):
                cur, color = q.get()
                visit.add((cur, color))
                if ans[cur] == -1:
                    ans[cur] = lv
                color ^= 1
                for node in mat[color][cur]:
                    if (node, color) not in visit:
                        q.put((node, color))
            lv += 1
        return ans