class Node:
    def __init__(self, key, val, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next
        
class DoubLinkList:
    def __init__(self):
        self.current = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def add(self, node): # 在链表尾部添加元素
        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node
        self.current += 1
    
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.current -= 1
        return node

    def get_size(self):
        return self.current

    def remove_lru(self):
        return self.remove(self.head.next)

class LRUCache:

    def __init__(self, capacity: int):
        self.list = DoubLinkList()
        self.map = {}
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        target = self.map[key]
        self.list.remove(target) # O(1)
        self.list.add(target) # O(1)
        return target.val

    def put(self, key: int, value: int) -> None:
        if key in self.map: # O(1)
            target = self.map[key]
            self.list.remove(target)
            target.val = value
            self.list.add(target)
            self.map[key] = target
        else: # O(1)
            if self.list.get_size() == self.size:
                node = self.list.remove_lru()
                del self.map[node.key]
            self.map[key] = Node(key, value)
            self.list.add(self.map[key])



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)