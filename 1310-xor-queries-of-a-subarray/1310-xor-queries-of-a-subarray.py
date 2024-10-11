class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        xor = [0]*(n+1)
        ans = []
        
        for i in range(1, n+1):
            xor[i] = xor[i-1]^arr[i-1]
            
        for start, end in queries:
            ans.append(xor[end+1]^xor[start])
            
        return ans
    
    # TC: O(q) + O(n)
    #     SC: O(n)
    #         Approach: We can create a prefix xor array, and for the given range use xor(end+1)^xor(start)
        