class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1
        
        def count_steps(curr):
            nex, cnt = curr + 1, 0
            while curr <= n:
                diff = min(nex, n+1) - curr
                cnt += diff
                curr *= 10
                nex *= 10
                
            return cnt
        
        while k>0:
            steps = count_steps(curr)
            if steps > k:
                curr *= 10
                k -= 1
            else:
                curr += 1
                k -= steps
            
            
        return curr
        