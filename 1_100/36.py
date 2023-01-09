class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # # 1. 每行一个字典，每列一个字典, 每个九宫格一个字典
        # from collections import defaultdict
        # rows = [defaultdict(int) for i in range(9)]
        # cols = [defaultdict(int) for i in range(9)]
        # wins = [defaultdict(int) for i in range(9)]
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] != '.':
        #             rows[i][board[i][j]] += 1
        #             cols[j][board[i][j]] += 1
        #             wins[i//3*3+j//3][board[i][j]] += 1
        #             if rows[i][board[i][j]] > 1 or cols[j][board[i][j]] > 1 or wins[i//3*3+j//3][board[i][j]] > 1:
        #                 return False
        # return True

        # 2. 类似1, 存储格式变成数组
        rows = [[0 for i in range(9)] for j in range(9)]
        cols = [[0 for i in range(9)] for j in range(9)]
        wins = [[[0 for i in range(9)] for j in range(3)] for k in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    index = int(board[i][j]) - 1
                    rows[i][index] += 1
                    cols[j][index] += 1
                    wins[i//3][j//3][index] += 1
                    if rows[i][index] > 1 or cols[j][index] > 1 or wins[i//3][j//3][index] > 1:
                        return False
        return True