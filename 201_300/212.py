class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. 暴力回溯，最后两样例超时
        # rows, cols = len(board), len(board[0])
        # flag = [[False] * cols for i in range(rows)]
        # result = []
        #
        # def dfs(board, index, target, row, col, flag):
        #     """
        #     :param board: 原矩阵
        #     :param index: 正在匹配的字符串索引
        #     :param target: 需要匹配的字符串
        #     :param row: 当前行
        #     :param col: 当前列
        #     :param flag: 表示矩阵中每个元素是否访问
        #     :return:
        #     """
        #     if index == len(target): # 结束条件
        #         return True
        #     if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or flag[row][col] or \
        #         target[index] != board[row][col]:
        #         return False
        #     # 当前字符已满足，进行下一个字符的匹配
        #     flag[row][col] = True
        #     result = dfs(board, index + 1, target, row - 1, col, flag) or \
        #              dfs(board, index + 1, target, row + 1, col, flag) or \
        #              dfs(board, index + 1, target, row, col - 1, flag) or \
        #              dfs(board, index + 1, target, row, col + 1, flag)
        #     flag[row][col] = False
        #     return result
        #
        # for word in words:
        #     for i in range(rows):
        #         for j in range(cols):
        #             if board[i][j] == word[0] and not flag[i][j] and dfs(board, 0, word, i, j, flag):
        #                 result.append(word)
        # return list(set(result))

        # 2. 前缀集合, 通过了
        rows, cols = len(board), len(board[0])
        flag = [[False] * cols for i in range(rows)]
        self.result = []
        trieSet = set()
        for word in words:
            for i in range(len(word)):
                if word[:i + 1] not in trieSet:
                    trieSet.add(word[:i + 1])

        def dfs(board, prefix, trieSet, words, row, col, flag):
            """
            :param board: 原矩阵
            :param prefix: 目前组成的字符串
            :param trieSet: 前缀字符串集合
            :param words: 目标字符串集合
            :param row: 当前行
            :param col: 当前列
            :param flag: 判断是否访问
            :return:
            """
            # 返回条件1
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or flag[row][col]:
                return
            prefix += board[row][col]
            # 返回条件2
            if prefix not in trieSet:
                return
            if prefix in words:
                self.result.append(prefix)
            # 当前字符已满足，进行下一个字符的匹配
            flag[row][col] = True
            dfs(board, prefix, trieSet, words, row - 1, col, flag)
            dfs(board, prefix, trieSet, words, row + 1, col, flag)
            dfs(board, prefix, trieSet, words, row, col - 1, flag)
            dfs(board, prefix, trieSet, words, row, col + 1, flag)
            flag[row][col] = False

        for i in range(rows):
            for j in range(cols):
                dfs(board, '', trieSet, words, i, j, flag)
        return list(set(self.result))