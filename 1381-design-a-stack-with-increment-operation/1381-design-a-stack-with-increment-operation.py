class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.maxSize = maxSize
        self.count = 0
        

    def push(self, x: int) -> None:
        if self.count == self.maxSize:
            return
        self.count += 1
        self.arr.append(x)
        

    def pop(self) -> int:
        if self.count == 0:
            return -1
        val = self.arr.pop(self.count-1)
        self.count -= 1
        return val
        

    def increment(self, k: int, val: int) -> None:
        k = min(k, self.count)
        for i in range(k):
            self.arr[i] = self.arr[i]+val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)