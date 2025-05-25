class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mem = defaultdict(int)
        ans = 0
        
        words.sort()

        for word in words:
            rev_w = word[::-1]
            if rev_w in mem:
                ans += 4
                mem[rev_w] -= 1
                if mem[rev_w] == 0:
                    del mem[rev_w]
            else:
                mem[word] += 1

        for key, val in mem.items():
            if key[0] == key[1] and val > 0:
                ans += 2
                break

        return ans

