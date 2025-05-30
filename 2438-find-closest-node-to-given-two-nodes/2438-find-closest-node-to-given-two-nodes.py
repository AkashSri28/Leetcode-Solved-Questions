class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        node1_dis = [-1]*n
        node2_dis = [-1]*n

        def find_dis(node_dis, node):
            node_dis[node] = 0
            cnt = 1
            while edges[node] != -1 and node_dis[edges[node]] == -1:
                node_dis[edges[node]] = cnt 
                cnt += 1
                node = edges[node]

        find_dis(node1_dis, node1)
        find_dis(node2_dis, node2)

        ans = -1
        dis = float('inf')
        for i in range(n):
            if min(node1_dis[i], node2_dis[i]) == -1:
                continue
            if dis > max(node1_dis[i], node2_dis[i]):
                dis = max(node1_dis[i], node2_dis[i])
                ans = i

        return ans
            

        