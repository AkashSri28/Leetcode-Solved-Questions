class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        n = len(words)
        words.sort(key=len, reverse=True)
        for i in range(n):
            for j in range(i+1, n):
                if words[j] in words[i]:
                    ans.add(words[j])

        return list(ans)

        # TC: O(nlogn) + O(n^2*m)
        # SC: O(n^2)
        # Approach: Since constraints are weak, we can use brute force here. Compare all strings and check if any string is substring
        # Sort in descending order to avoid re-comparisons

