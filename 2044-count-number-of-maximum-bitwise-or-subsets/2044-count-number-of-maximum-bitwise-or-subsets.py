class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_val = float('-inf')
        mem = defaultdict(int)
        
        def helper(index, val):
            nonlocal max_val
            if index == len(nums):
                max_val = max(max_val, val)
                mem[val] += 1
                return
                
            helper(index+1, val|nums[index])
            helper(index+1, val)
        
        helper(0, 0)
                
        return mem[max_val]
    
    # TC: O(2**n)
    #     SC: O(n)
    #         Approach: Find all subsets and check or
        