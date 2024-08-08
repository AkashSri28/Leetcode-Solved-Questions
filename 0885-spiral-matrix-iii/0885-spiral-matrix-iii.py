class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ls = list(range(rows*cols))
        counter, i, j = 1, rStart, cStart
        ans = []
        
        def valid(i, j):
            nonlocal rows, cols
            return i >=0 and j >= 0 and i < rows and j < cols 
        
        while len(ls) > 0:
            for k in range(counter):
                if valid(i, j):
                    ans.append([i, j])
                    val = i*cols+j
                    ls.remove(val)
                j += 1
                
                
            for k in range(counter):
                if valid(i, j):
                    ans.append([i, j])
                    val = i*cols+j
                    ls.remove(val)
                i += 1
            counter += 1
                
            for k in range(counter):
                if valid(i, j):
                    ans.append([i, j])
                    val = i*cols+j
                    ls.remove(val)
                j -= 1
                
            for k in range(counter):
                if valid(i, j):
                    ans.append([i, j])
                    val = i*cols+j
                    ls.remove(val)
                i -= 1
            counter += 1
                
        return ans
                
            
        
        
            
        