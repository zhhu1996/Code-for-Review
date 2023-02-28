class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        """迷宫III
        1. BFS + distrika最短路径
        """
        from queue import Queue

        directions = [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]
        m, n = len(maze), len(maze[0])
        distance = [[float('inf') for _ in range(n)] for i in range(m)]
        string = [['impossible' for _ in range(n)] for i in range(m)]
        q = Queue(-1)
        q.put((ball[0], ball[1]))
        distance[ball[0]][ball[1]] = 0
        string[ball[0]][ball[1]] = ""

        while not q.empty():
            row, col = q.get()
            for dr, dc, d in directions:
                cur_r, cur_c = row, col
                step, word = distance[cur_r][cur_c], string[cur_r][cur_c]
                while 0<=cur_r+dr<m and 0<=cur_c+dc<n and maze[cur_r+dr][cur_c+dc] == 0 and not (cur_r==hole[0] and cur_c==hole[1]):
                    cur_r += dr
                    cur_c += dc
                    step += 1 
                if distance[cur_r][cur_c] > step or (distance[cur_r][cur_c] == step and word+d < string[cur_r][cur_c]):
                    distance[cur_r][cur_c] = step
                    string[cur_r][cur_c] = word + d
                    if not (cur_r == hole[0] and cur_c == hole[1]):
                        q.put((cur_r, cur_c))
        
        return string[hole[0]][hole[1]]