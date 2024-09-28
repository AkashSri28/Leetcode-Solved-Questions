class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [0]*k
        self.start = 0
        self.end = 0
        self.k = k
        self.count = 0
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.start = (self.start-1)%self.k
        self.arr[self.start] = value
        self.count += 1   
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.end] = value
        self.end = (self.end+1)%self.k
        self.count += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.start = (self.start+1)%self.k
        self.count -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.end = (self.end-1)%self.k
        self.count -= 1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.start]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.end-1)%self.k]
        

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.count == self.k:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()