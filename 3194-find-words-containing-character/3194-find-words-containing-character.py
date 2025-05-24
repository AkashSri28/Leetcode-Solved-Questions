class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for index, word in enumerate(words):
            if x in word:
                ans.append(index)
        return ans

        # TC: O(n)
        # SC: O(1)
        # Approach: Check if x exists in all words, store index if x in word