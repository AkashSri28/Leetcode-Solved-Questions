class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = right = 0
        ans = 0
        cnt = 0
        for i in range(k):
            if blocks[i] == 'W':
                cnt += 1
            right = i

        ans = cnt
        while right+1 < len(blocks):
            if blocks[left] == 'W':
                cnt -= 1
            left += 1
            if blocks[right+1] == 'W':
                cnt += 1
            right += 1
            ans = min(ans, cnt)

        return ans
        
        