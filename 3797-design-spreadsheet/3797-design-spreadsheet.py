class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0]*26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col, row = cell[0], int(cell[1:])
        self.grid[row-1][ord(col)-ord('A')] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getCell(self, cell:str) -> None:
        col, row = cell[0], int(cell[1:])
        print(col," ",row)
        return self.grid[row-1][ord(col)-ord('A')]

    def getValue(self, formula: str) -> int:
        expr = formula.lstrip('=')
        left, right = expr.split('+')
        ans = 0
        if left[0].isalpha():
            ans += self.getCell(left)
        else:
            ans += int(left)

        if right[0].isalpha():
            ans += self.getCell(right)
        else:
            ans += int(right)
        return ans

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)