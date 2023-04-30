class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """钥匙和房间
        1. dfs
        dfs遍历图的节点, 可以全部到达就返回True

        2. bfs
        """
        # # 1.
        # n = len(rooms)
        # visited = [False]*n
        # self.keys = 0

        # def dfs(room):
        #     visited[room] = True
        #     self.keys += 1
        #     for key in rooms[room]:
        #         if not visited[key]:
        #             dfs(key)

        # dfs(0)
        # return self.keys == n


        # 2.
        from queue import Queue
        n = len(rooms)
        visited = [False]*n
        q = Queue(-1)
        q.put(0)
        visited[0] = True
        keys = 1
        while not q.empty():
            cur = q.get()
            for key in rooms[cur]:
                if not visited[key]:
                    q.put(key)
                    visited[key] = True
                    keys += 1
        return keys == n