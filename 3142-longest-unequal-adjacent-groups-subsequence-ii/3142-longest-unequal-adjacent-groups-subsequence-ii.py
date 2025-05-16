class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [[] for _ in range(n)]

        def compare(word1, word2):
            if len(word1) != len(word2):
                return False
            cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    cnt += 1
                    if cnt == 2:
                        return False
            return True

        for j in range(n-1, -1, -1):
            dp[j].append(words[j])
            max_path = 1
            ans = j
            for i in range(j+1, n):
                if groups[i] != groups[j] and compare(words[j], words[i]):
                    if 1+len(dp[i]) > max_path:
                        max_path = 1 + len(dp[i])
                        ans = i
            if ans != j:
                dp[j] = dp[j]+dp[ans]

        res = []

        for i in range(n):
            if len(dp[i]) > len(res):
                res = dp[i]
        
        return res

        # TC: O(n^2*m)
        # SC: O(n*m)
        # Approach: for finding longest increasing sequence build ans from right to left. At each index of dp, store longest path starting from that index
        