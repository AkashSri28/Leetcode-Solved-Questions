class Solution:
    def largestCombination(self, nums: List[int]) -> int:
        bit_map = defaultdict(int)
        for n in nums:
            pos = 1
            while n > 0:
                if n & 1 == 1:
                    bit_map[pos] += 1
                pos += 1
                n = n >> 1
        
        ans = max(bit_map.values())
            
        return ans
    
#     TC: O(2n)
#         SC: O(n)
#             Approach: max length queue will be where same bits are set. Use dict to store length of each and find max in end.
        