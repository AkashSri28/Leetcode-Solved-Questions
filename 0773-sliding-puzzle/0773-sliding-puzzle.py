class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = '123450'
        visited = set()
        
        s = ''
        neigh = {
            0:[1,3],
            1:[0,2,4],
            2:[1,5],
            3:[0,4],
            4:[3,1,5],
            5:[2,4]
        }
        
        for i in range(2):
            for j in range(3):
                s = s+str(board[i][j])
                
        ind = s.index('0')
        
        q = deque()
        q.append((s, ind, 0))
        
        while q:
            curr, ind, moves = q.popleft()
            if curr == target:
                return moves
            if curr not in visited:
                visited.add(curr)
                
            for n in neigh[ind]:
                ls = list(curr)
                ls[ind], ls[n] = ls[n], ls[ind]
                nex = ''.join(ls)
                if nex not in visited:
                    q.append((nex, n, 1+moves))            
            
        return -1
                