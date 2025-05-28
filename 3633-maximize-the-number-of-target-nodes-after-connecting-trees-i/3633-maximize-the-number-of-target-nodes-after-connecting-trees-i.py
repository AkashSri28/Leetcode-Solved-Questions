class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1)+1
        m = len(edges2)+1
        nodes_cnt = [0]*n
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)

        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        max_cnt = 0
        for i in range(m):
            q = deque()
            visited = set()
            q.append((i, 0))
            cnt = 0
            while q:
                node, dis = q.popleft()
                visited.add(node)
                if dis <= k-1:
                    cnt += 1
                    for nei in adj2[node]:
                        if nei not in visited:
                            q.append((nei, dis+1))

            max_cnt = max(max_cnt, cnt)

        for i in range(n):
            q = deque()
            visited = set()
            q.append((i, 0))
            cnt = 0
            while q:
                node, dis = q.popleft()
                visited.add(node)
                if dis <= k:
                    cnt += 1
                    for nei in adj1[node]:
                        if nei not in visited:
                            q.append((nei, dis+1))

            nodes_cnt[i] = cnt+max_cnt

        return nodes_cnt

        

        



        