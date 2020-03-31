class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        flag = [[False] * cols for i in range(rows)]

        def dfs(board, index, target, row, col, flag):
            """
            :param board: 原矩阵
            :param index: 正在匹配的字符串索引
            :param target: 需要匹配的字符串
            :param row: 当前行
            :param col: 当前列
            :param flag: 表示矩阵中每个元素是否访问
            :return:
            """
            if index == len(target): # 结束条件
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or flag[row][col] or target[index] != board[row][col]: # 不满足的条件
                return False
            # 当前字符已满足，进行下一个字符的匹配
            flag[row][col] = True
            result = dfs(board, index + 1, target, row - 1, col, flag) or \
                     dfs(board, index + 1, target, row + 1, col, flag) or \
                     dfs(board, index + 1, target, row, col - 1, flag) or \
                     dfs(board, index + 1, target, row, col + 1, flag)
            flag[row][col] = False
            return result

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and not flag[i][j] and dfs(board, 0, word, i, j, flag):
                    return True
        return False
