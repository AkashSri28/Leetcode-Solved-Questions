class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        prev = [0]*26
        MOD = 1000000007

        for ch in s:
            prev[ord(ch)-ord('a')] += 1
        
        for i in range(t):
            curr = [0]*26

            for j in range(25):
                curr[j+1] = prev[j]

            curr[0] = prev[25]
            curr[1] = (curr[1]+prev[25])%MOD

            prev = curr

        return sum(prev)%MOD
        