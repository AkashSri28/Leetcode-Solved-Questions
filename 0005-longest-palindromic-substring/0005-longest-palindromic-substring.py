class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        n = len(s)
        
        def check_longest_palindrome(s, i):
            nonlocal ans
            j = k = i
            pal_len = 0
            while j >= 0 and k < n and s[j] == s[k]:
                pal_len = (k-j)+1
                j -= 1
                k += 1
                
            if pal_len > len(ans):
                ans = s[j+1:k]
                
            j = i
            k = i+1
            pal_len = 0
            while j >= 0 and k < n and s[j] == s[k]:
                pal_len = (k-j)+1
                j -= 1
                k += 1
                
            if pal_len > len(ans):
                ans = s[j+1:k]
                
        
        #for every char we can check if it is center of any palindrome
        for i in range(len(s)):
            check_longest_palindrome(s, i)
            
        return ans
    
    # TC: O(n^2)
    #     SC: O(1)
    #         Approach: for every index check the maximum palindrome length possible at that index