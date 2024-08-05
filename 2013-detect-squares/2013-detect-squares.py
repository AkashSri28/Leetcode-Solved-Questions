class DetectSquares:

    def __init__(self):
        self.obj = defaultdict(list)
        

    def add(self, point: List[int]) -> None:
        self.obj[point[0]].append(point[1])

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        y_values = self.obj[x1]
        ans = 0
        
        for y2 in y_values:
            if y2 == y1:
                continue
            x2 = x1 - abs(y2 - y1)
            if x2 in self.obj:
                count1 = self.obj[x2].count(y1)
                count2 = self.obj[x2].count(y2)
                ans += (count1*count2)
                
            x3 = x1 + abs(y2 - y1)
            if x3 in self.obj:
                count1 = self.obj[x3].count(y1)
                count2 = self.obj[x3].count(y2)
                ans += (count1*count2)
                
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)