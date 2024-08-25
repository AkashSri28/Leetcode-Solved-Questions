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
        char_n = list(n)
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
            
        
        