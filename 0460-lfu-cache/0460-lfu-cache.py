class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _addToFront(self, node):
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        node.prev = self.head

    def isEmpty(self):
        return self.head.next == self.tail

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        self.freqMap = dict()
        self.size = 0      
        self.minFreq = 0  

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        freq = node.freq
        self.freqMap[freq]._remove(node)

        if freq == self.minFreq and self.freqMap[freq].isEmpty():
            del self.freqMap[freq]
            self.minFreq += 1

        node.freq += 1
        if freq + 1 not in self.freqMap:
            self.freqMap[freq+1] = DoublyLinkedList()
        self.freqMap[freq+1]._addToFront(node)
        return node.val       

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value

            freq = node.freq
            self.freqMap[freq]._remove(node)
            if freq == self.minFreq and self.freqMap[freq].isEmpty():
                del self.freqMap[freq]
                self.minFreq += 1
            
            node.freq += 1
            if freq + 1 not in self.freqMap:
                self.freqMap[freq+1] = DoublyLinkedList()
            self.freqMap[freq+1]._addToFront(node)
            return

        if self.capacity == self.size:
            ll = self.freqMap[self.minFreq]
            node = ll.tail.prev
            ll._remove(node)
            if ll.isEmpty():
                self.minFreq += 1
            del self.map[node.key]
            self.size -= 1

        node = Node(key, value)
        self.minFreq = 1
        self.map[key] = node
        if self.minFreq not in self.freqMap:
            self.freqMap[self.minFreq] = DoublyLinkedList()
        self.freqMap[self.minFreq]._addToFront(node) 
        self.size += 1
            

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)