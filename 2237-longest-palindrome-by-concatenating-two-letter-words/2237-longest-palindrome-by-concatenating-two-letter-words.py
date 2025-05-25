class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mem = defaultdict(int)
        ans = 0

        for word in words:
            rev_w = word[::-1]
            if mem[rev_w] > 0:
                ans += 4
                mem[rev_w] -= 1
            else:
                mem[word] += 1

        for key, val in mem.items():
            if key[0] == key[1] and val > 0:
                ans += 2
                break

        return ans

        # TC: O(n)
        # SC: O(n)
        # Approach: we need to find word and its reverse, hence map will be used to track history. Now if a word has both char equal it can be placed in middle after using all pairs

