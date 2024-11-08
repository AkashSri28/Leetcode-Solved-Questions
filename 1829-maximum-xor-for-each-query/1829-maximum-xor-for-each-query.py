class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        k = 2**maximumBit - 1
        n = len(nums)
        prefix = [0]
        
        for num in nums:
            res = prefix[-1]^num
            prefix.append(res)
            
        answer = []
        
        for i in range(n, 0, -1):
            res = prefix[i]^k
            answer.append(res)
            
        return answer
    
    # TC O(2N)
    # SC O(N)
    # Approach To find max value of k, we need to find the value XOR of value calculated so far and max value possible.  
        