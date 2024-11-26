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
    
    # TC: O(n)
    #     SC: O(n)
    #         Approach: A team will be strongest, if there is no incoming edge. Store in-degree of all nodes. Now if there are more than 1 node with in-degree 0, return -1
        