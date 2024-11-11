class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def is_prime(a):
            for i in range(2, a):
                if a%i == 0:
                    return False
            return True
        
        def next_num(a, b):
            for i in range(2, a):
                if is_prime(i) and a-i < b:
                    return a-i
            return -1
        
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                continue
            nums[i] = next_num(nums[i], nums[i+1])
            if nums[i] <= 0:
                return False
            
        return True
        