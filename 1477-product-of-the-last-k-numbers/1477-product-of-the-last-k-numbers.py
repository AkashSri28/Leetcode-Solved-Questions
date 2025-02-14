class ProductOfNumbers:

    def __init__(self):
        self.ls = []
        self.prod = 1
        

    def add(self, num: int) -> None:
        if num == 0:
            self.ls = []
            self.prod = 1
        else:
            self.prod *= num
            self.ls.append(self.prod)
        

    def getProduct(self, k: int) -> int:
        if k > len(self.ls):
            return 0
        elif k < len(self.ls):
            return self.ls[-1]//self.ls[-(k+1)]
        else:
            return self.ls[-1]

    # TC: add - O(1), getProduct - O(1)
    # SC: O(k)
    # Approach: if we get a 0 as input, all the products including it will be 0. Hence we can restart the list once we see a 0.

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)