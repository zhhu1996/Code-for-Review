class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """活字印刷
        1. 有重复数字的全排列问题
        """
        # 方法1
        self.result = []

        def dfs(tiles, path, visited):
            if len(path) == len(tiles):
                self.result.append(path.copy())
                return
            if path:
                self.result.append(path.copy())
            for i in range(len(tiles)):
                if visited[i]:
                    continue
                if i > 0 and tiles[i] == tiles[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                path.append(tiles[i])
                dfs(tiles, path, visited)
                visited[i] = False
                path.pop()

        n = len(tiles)
        array = list(sorted(tiles))
        visited = [False] * n
        dfs(array, [], visited)
        return len(self.result)

