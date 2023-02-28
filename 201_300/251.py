class Vector2D:
    """展开二维向量
    1. 双指针
    """
    
    def __init__(self, vec: List[List[int]]):
        self.res = vec
        self.len = len(vec)
        self.cur_row = 0
        self.cur_col = -1
        self.next_row = 0
        self.next_col = 0

    def next(self) -> int:
        if self.hasNext():
            self.cur_row = self.next_row
            self.cur_col = self.next_col
            return self.res[self.cur_row][self.cur_col]

    def hasNext(self) -> bool:
        if len(self.res) == 0:
            return False
        cur_len = len(self.res[self.cur_row])
        row_offset, col_offset = 1, 1
        if self.cur_col + col_offset < cur_len:
            self.next_row = self.cur_row
            self.next_col = self.cur_col + col_offset
            return True
        else:
            while self.cur_row + row_offset < self.len and len(self.res[self.cur_row+row_offset]) == 0:
                row_offset += 1
            if self.cur_row + row_offset < self.len:
                self.next_row = self.cur_row + row_offset
                self.next_col = 0
                return True
            else:
                return False



# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()