class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = dict()   # (key, node)        
        self.capacity = capacity
        self.size = 0

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _addToFront(self, node):
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._addToFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._addToFront(node)
            return

        if self.capacity == self.size:
            node = self.tail.prev
            self._remove(node)
            del self.map[node.key]
            self.size -= 1

        node = Node(key, value)
        self.map[key] = node
        self._addToFront(node)
        self.size += 1     

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)