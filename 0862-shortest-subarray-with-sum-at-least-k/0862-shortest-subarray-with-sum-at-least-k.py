class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n, ans, curr_sum = len(nums), len(nums)+1, 0
        q = deque() 
        
        for i in range(n):
            curr_sum += nums[i]
            
            if curr_sum >= k:
                ans = min(ans, i+1)
                
            while q and curr_sum - q[0][0] >= k:
                s, index = q.popleft()
                ans = min(ans, i-index)
                
            while q and q[-1][0] > curr_sum:
                q.pop()
                
            q.append((curr_sum ,i))
            
        return -1 if ans == n+1 else ans
        