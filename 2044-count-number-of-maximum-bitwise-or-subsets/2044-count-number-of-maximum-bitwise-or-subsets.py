class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_val = 0
        for n in nums:
            max_val |= n
        # mem = defaultdict(int)
        
        res = 0
        
        def helper(index, val):
            nonlocal max_val, res
            if index == len(nums):
                # max_val = max(max_val, val)
                # mem[val] += 1
                if val == max_val:
                    res += 1
                return
                
            helper(index+1, val|nums[index])
            helper(index+1, val)
        
        helper(0, 0)
                
        return res
    
    # TC: O(2**n)
    #     SC: O(n)
    #         Approach: Find all subsets and check or
        