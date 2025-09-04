class MyQueue:

    def __init__(self):
        self.s1 = [] # will be used for push
        self.s2 = [] # will be used for pop
        
    def push(self, x: int) -> None:
        self.s1.append(x)
        
    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()        

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        if not self.s2 and not self.s1:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()           TC
# obj.push(x)               O(1)
# param_2 = obj.pop()       O(n) or O(1)
# param_3 = obj.peek()      O(n) or O(1)
# param_4 = obj.empty()     O(1)

# Approach: we will use 2 stacks here, s1 for push and s2 for pop. If s2 is empty, we will transfer all elements from s1 into s2