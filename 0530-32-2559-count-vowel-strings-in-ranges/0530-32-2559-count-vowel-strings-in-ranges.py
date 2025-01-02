class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def checkWord(word):
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                return 1
            return 0

        n = len(words)
        prefix = [0]*(n+1)

        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + checkWord(words[i-1])
        
        ans = []
        for start, end in queries:
            ans.append(prefix[end+1] - prefix[start])

        return ans

        