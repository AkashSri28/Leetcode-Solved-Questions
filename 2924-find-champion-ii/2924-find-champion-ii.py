class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0]*n
        
        for u, v in edges:
            in_degree[v] += 1
            
        ans = -1
        
        for index, e in enumerate(in_degree):
            if e == 0:
                if ans != -1:
                    return -1
                ans = index
                
        return ans
        