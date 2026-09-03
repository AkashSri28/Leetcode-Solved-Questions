class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low, high = 1, m*n
        ans = 1
        while low <= high:
            mid = (low + high)//2
            cnt = 0
            for i in range(1, m+1):
                cnt += min(mid//i, n)
            if cnt >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        
# Clarification: can check for range of m and n
# Brute Force: check all numbers between 1 and m*n, kth element will be ans, TC O(m*n)
# Approach: so answer will be between 1 and m*n, so BS can be tried here (hint). Now for each row check number of elements that will be less than mid guessed. min(mid // i, n) will give the numbers less than mid in each row. if cnt >= k then move left, else move right.
# why min(mid // i, n)? since in each row m will be constant, only n will vary, hence dividing mid by m for that row will give position of n, now min(mid//i, n) will tell the value of n if less than n or else it will take n
# TC: O(n)
# SC: O(1)
# Testing:
