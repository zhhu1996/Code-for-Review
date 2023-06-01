class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """循环轮转矩阵
        1. 模拟
        每一圈的左上角(i,i), 左下角(m-1-i, i), 右下角(m-1-i, n-1-i), 右上角(i,n-1-i)
        每一圈长度为(m-2i)*2+(n-2i-2)*2 = 2*(m+n-4i-2)
        """
        i, m, n = 0, len(grid), len(grid[0])
        while i < min(m,n) // 2:
            p1, p2, p3, p4 = (i, i), (m-1-i, i), (m-1-i, n-1-i), (i, n-1-i)
            # collect
            arr = []
            for row in range(i, m-i-1):
                arr.append(grid[row][i])
            for col in range(i, n-i-1):
                arr.append(grid[m-1-i][col])
            for row in range(m-1-i, i, -1):
                arr.append(grid[row][n-1-i])
            for col in range(n-1-i, i, -1):
                arr.append(grid[i][col])
            # rotate
            lth = 2*(m+n-4*i-2)
            assert lth == (m-2*i)*(n-2*i) - (m-2*(i+1))*(n-2*(i+1))
            assert lth == len(arr)
            kk = k % lth
            arr = arr[-kk:] + arr[:-kk]
            # insert
            index = 0
            for row in range(i, m-i-1):
                grid[row][i] = arr[index]
                # grid[row][i] = arr[(index+lth-k)%lth]
                index += 1
            for col in range(i, n-i-1):
                grid[m-1-i][col] = arr[index]
                # grid[m-1-i][col] = arr[(index+lth-k)%lth]
                index += 1
            for row in range(m-1-i, i, -1):
                grid[row][n-1-i] = arr[index]
                # grid[row][n-1-i] = arr[(index+lth-k)%lth]
                index += 1
            for col in range(n-1-i, i, -1):
                grid[i][col] = arr[index]
                # grid[i][col] = arr[(index+lth-k)%lth]
                index += 1            
            i += 1
        return grid