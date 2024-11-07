class Solution:
    def largestCombination(self, nums: List[int]) -> int:
        bit_map = defaultdict(list)
        for n in nums:
            pos = 1
            while n > 0:
                if n & 1 == 1:
                    bit_map[pos].append(n)
                pos += 1
                n = n >> 1
        
        ans = 0
        for v in bit_map.values():
            ans = max(ans, len(v))
            
        return ans
        