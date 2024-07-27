class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        #construct graph
        INF = float('inf')
        
        distance = [[float('inf')]*26 for _ in range(26)]
        
        for i in range(26):
            distance[i][i] = 0
            
        def char_to_index(ch):
            return ord(ch) - ord('a')
            
        # Update the distance matrix with the given edges
        for i in range(len(original)):
            u = char_to_index(original[i])
            v = char_to_index(changed[i])
            distance[u][v] = min(distance[u][v], cost[i])     
        
        #Floyd Worshall Algorithm
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if distance[i][k] < INF and distance[k][j] < INF:
                        distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        res = 0             
        for i in range(len(source)):
            u = char_to_index(source[i])
            v = char_to_index(target[i])
            if distance[u][v] == INF:
                return -1
            res += distance[u][v]        
        return res
        
        
        