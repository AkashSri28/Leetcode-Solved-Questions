class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        def validMatrix(r1, r2, c1, c2):
            temp = [0]*10
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    val = board[i][j]
                    if val == ".":
                        continue
                    val = int(val)
                    temp[val] += 1
                    if temp[val] > 1:
                        return False
            return True


        for i in range(9):
            if not validMatrix(i, i, 0, 8):
                return False

        for j in range(9):
            if not validMatrix(0, 8, j, j):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not validMatrix(i, i+2, j, j+2):
                    return False

        return True

        TC: O(1)
        SC: O(1)

        