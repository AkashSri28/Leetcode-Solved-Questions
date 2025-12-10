class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [0]*(k+1)
        self.k = k+1
        self.f = 0
        self.r = 0
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.f = (self.f - 1 + self.k) % self.k
        self.arr[self.f] = value
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.r] = value
        self.r = (self.r+1)%self.k
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.f = (self.f+1)%self.k
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.r = (self.r - 1 + self.k) % self.k
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.f]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.r - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        return self.f == self.r

    def isFull(self) -> bool:
        return (self.r+1)%self.k == self.f
        


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