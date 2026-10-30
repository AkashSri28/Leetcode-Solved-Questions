class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node    
        node.next.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.key

    def get(self, key: int) -> int:
        if self.size == 0:
            return -1
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.addNode(node)

            return node.val 
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.addNode(node)
            return 

        if self.size == self.capacity:
            k = self.remove(self.tail.prev)
            del self.map[k]
            self.size -= 1
        node = Node(key, value)
        self.map[key] = node
        self.addNode(node)
        self.size += 1


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)