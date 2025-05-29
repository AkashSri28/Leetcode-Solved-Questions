class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        N = len(edges1)+1
        M = len(edges2)+1

        color1 = [0]*N
        color2 = [0]*M

        def build(edges, color):
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

            q = deque()
            q.append((0, 1))
            vis = set()
            while q:
                node, p_color = q.popleft()
                color[node] = 1^p_color
                vis.add(node)
                for nei in adj[node]:
                    if nei not in vis:
                        q.append((nei, color[node]))

        def count(color):
            cnt_w = cnt_b = 0
            for i in range(len(color)):
                if color[i] == 0:
                    cnt_w += 1
                else:
                    cnt_b += 1
            return [cnt_w, cnt_b]

        build(edges1, color1)
        build(edges2, color2)

        cnt_w1, cnt_b1 = count(color1)
        cnt_w2, cnt_b2 = count(color2)
        cnt2 = max(cnt_w2, cnt_b2)

        ans = []
        for i in range(N):
            if color1[i] == 0:
                ans.append(cnt_w1+cnt2)
            else:
                ans.append(cnt_b1+cnt2)

        return ans

        # TC: O(M+N)
        # SC: O(M+N)
        # Approach: since we need to count odd and even nodes, we can color then to identify their count. Once we color, we can check count of each color in tree
        