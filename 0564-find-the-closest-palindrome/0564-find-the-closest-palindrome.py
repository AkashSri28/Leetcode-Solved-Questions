class Solution:
    def half_to_palindrome(self, tmp, is_even):
        rev = tmp
        if not is_even:
            tmp //= 10
            
        while tmp > 0:
            rev = rev*10 + tmp%10
            tmp //= 10
            
        return rev
    
    def nearestPalindromic(self, n: str) -> str:
        len_n = len(n)
        int_n = int(n)
        is_even = False
        if len_n % 2 == 0:
            is_even = True
        
        results = []
        
        mid = len_n//2 - 1 if is_even else len_n//2
        tmp = int(n[:mid+1])
        results.append(self.half_to_palindrome(tmp, is_even))
        
        tmp = int(n[:mid+1]) + 1
        results.append(self.half_to_palindrome(tmp, is_even))
        
        tmp = int(n[:mid+1]) - 1
        results.append(self.half_to_palindrome(tmp, is_even))
        
        tmp = 10**(len_n-1)
        results.append(tmp-1)
        
        tmp = 10**len_n
        results.append(tmp+1)
        
        ans = results[0]
        diff = float("inf")
        
        for res in results:
            if res == int_n:
                continue
            if abs(res-int_n) < diff:
                ans = res
                diff = abs(res-int_n)
            if abs(res-int_n) == diff:
                ans = min(res, ans)
        
        return str(ans)
            
# TC: O(n)
#     SC: O(1)
#         Approach: for making 123 as palindrome there are 3 options: 121 (no change in first half), 131 (first half incremented by 1) and 111 (first half decremented by 1)
#                 Also, 99 and 1001 can be solution if it is a 3 digit number
        
        