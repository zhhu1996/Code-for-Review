import random

class SkipNode:
    def __init__(self, val, max_level=0):
        self.val = val
        self.next = [None] * max_level

class Skiplist:

    def __init__(self):
        self.max_lv = 32
        self.prob = 0.5
        self.head = SkipNode(-1, self.max_lv)
        self.cur_lv = 0

    def random_level(self):
        level = 1
        while random.random() < self.prob and level < self.max_lv:
            level += 1
        return level

    def find(self, target):
        """找到所有层小于target的最大节点"""
        targets = [self.head]*self.max_lv
        cur = self.head
        for i in range(self.cur_lv-1, -1, -1):
            while cur.next[i] and cur.next[i].val < target:
                cur = cur.next[i]
            targets[i] = cur
        return targets

    def search(self, target: int) -> bool:
        """找到所有层第一个大于target的节点 -> 都不满足说明不在表中"""
        targets = self.find(target)
        next_node = targets[0].next[0]
        return next_node is not None and next_node.val == target
        
    def add(self, num: int) -> None:
        """新建插入节点 -> 找到所有层的前驱节点 -> 更新最高层数 -> 插入所有层"""
        # 新建插入节点 -> 找到所有层的前驱节点
        update = self.find(num)
        # 更新最高层数
        rand_lv = self.random_level()
        self.cur_lv = max(self.cur_lv, rand_lv)
        # 插入所有层
        add_node = SkipNode(num, self.max_lv)
        for i in range(self.cur_lv-1, -1, -1):
            add_node.next[i] = update[i].next[i]
            update[i].next[i] = add_node

    def erase(self, num: int) -> bool:
        """找到所有层与num相等的节点 -> 全部删除 -> 调整层高"""
        # 找到所有层与num相等的节点
        update = self.find(num)
        cur = update[0].next[0]
        if not cur or cur.val != num:
            return False
        # 删除
        for i in range(self.cur_lv):
            if update[i].next[i] != cur:
                break
            update[i].next[i] = cur.next[i]
        # 调整层高
        while self.cur_lv > 1 and not self.head.next[self.cur_lv-1]:
            self.cur_lv -= 1
        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)