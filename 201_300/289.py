class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """ 生命游戏
        方法1: 暴力计算，时间复杂度O(mn)，空间复杂度O(mn)

        方法2：原地算法，时间复杂度O(mn)，空间复杂度O(1)
        一共有四种细胞状态转换，分别是
        活 -> 活  1
        活 -> 死  -1
        死 -> 死  0
        死 -> 活  2
        """
        # # 方法1
        # m, n = len(board), len(board[0])
        # matrix = [[0] * (n + 2) for i in range(m + 2)]
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         matrix[i][j] = board[i - 1][j - 1]
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         temp = matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i - 1][j + 1] + matrix[i][j - 1] + matrix[i][
        #             j + 1] + \
        #                matrix[i + 1][j - 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        #         if matrix[i][j] == 1:
        #             if temp < 2 or temp > 3:
        #                 board[i - 1][j - 1] = 0
        #         else:
        #             if temp == 3:
        #                 board[i - 1][j - 1] = 1

        # 方法2
        m, n = len(board), len(board[0])
        neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(m):
            for j in range(n):
                temp = 0
                for neighbour in neighbours:
                    if i == 0 and neighbour[0] == -1:
                        continue
                    if i == m - 1 and neighbour[0] == 1:
                        continue
                    if j == 0 and neighbour[1] == -1:
                        continue
                    if j == n - 1 and neighbour[1] == 1:
                        continue
                    row = i + neighbour[0]
                    col = j + neighbour[1]
                    if board[row][col] == -1 or board[row][col] == 1:
                        temp += 1
                if board[i][j] == 1:
                    if temp < 2 or temp > 3:
                        board[i][j] = -1
                else:
                    if temp == 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1
