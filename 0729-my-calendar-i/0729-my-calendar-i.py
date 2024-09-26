class MyCalendar:

    def __init__(self):
        self.slots = []        

    def book(self, start: int, end: int) -> bool:
        node = self.slots
        pos = bisect.bisect(self.slots, [start, end])
        if pos > 0:
            if self.slots[pos-1][1] > start:
                return False
        if pos != len(self.slots):
            if self.slots[pos][0] < end:
                return False
        self.slots.insert(pos, [start, end])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)