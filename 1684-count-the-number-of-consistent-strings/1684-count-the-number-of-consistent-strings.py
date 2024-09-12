class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        ans = 0
        for word in words:
            cnt = 0
            for i in range(len(word)):
                if word[i] not in allowed_set:
                    break
                cnt += 1
            if cnt == len(word):
                ans += 1
                
        return ans
        