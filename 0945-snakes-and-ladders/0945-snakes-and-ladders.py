class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # n = len(board)
        # q = deque()
        # q.append((1, 0))
        # vis = set()
        # while q:
        #     node, cnt = q.popleft()
        #     if node == n*n:
        #         return cnt
        #     vis.add(node)
        #     i = (n-1)-(node-1)//n
        #     j = (node-1)%n
        #     if (n-1-i)&1 == 1:
        #         j = n-1-j
        #     if board[i][j] != -1:
        #         q.append((board[i][j], cnt))
        #     else:
        #         for k in range(node+1, min(node+7, n*n+1)):
        #             if k not in vis:
        #                 q.append((k, cnt+1))

        # return -1
        n = len(board)
        
        def get_rc(pos):
            quot, rem = divmod(pos - 1, n)
            row = n - 1 - quot
            col = rem if (quot % 2 == 0) else n - 1 - rem
            return row, col

        visited = set()
        q = deque()
        q.append((1, 0))  # (cell number, moves)

        while q:
            pos, moves = q.popleft()
            if pos == n * n:
                return moves
            for next_pos in range(pos + 1, min(pos + 6, n * n) + 1):
                r, c = get_rc(next_pos)
                dest = board[r][c] if board[r][c] != -1 else next_pos
                if dest not in visited:
                    visited.add(dest)
                    q.append((dest, moves + 1))

        return -1


        