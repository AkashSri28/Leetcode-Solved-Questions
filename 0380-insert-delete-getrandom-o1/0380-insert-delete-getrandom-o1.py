class RandomizedSet:

    def __init__(self):
        self.map = dict()
        

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = val
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        del self.map[val]
        return True
        

    def getRandom(self) -> int:
        random_key = random.choice(list(self.map.keys()))
        return self.map[random_key]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# TC: O(1)
#     SC: O(n)
#         Approach: using a dictionary can help in accessing an object in O(1) time