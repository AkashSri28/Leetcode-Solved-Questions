class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        n, i = len(words), 0

        while i < n:
            j = i + 1
            while j < n and groups[j] == groups[j-1]:
                j += 1

            ans.append(words[i])
            i = j

        return ans

        # TC: O(n)
        # SC: O(1)
        # Approach: since we need to take word from alternating group, so find every group and take first word from that group

        