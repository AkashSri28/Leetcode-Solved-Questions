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
        
        