class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans_l = 0
        ans_r = 0
        ans_len = float('inf')
        freq = Counter(t)
        n = len(freq)
        left = 0
        mem = defaultdict(int)
        cnt = 0

        for right in range(len(s)):
            if s[right] in freq:
                mem[s[right]] += 1

                if mem[s[right]] == freq[s[right]]:
                    cnt += 1
                
                while cnt == n:
                    if s[left] in mem:
                        mem[s[left]] -= 1
                        if mem[s[left]] < freq[s[left]]:
                            cnt -= 1
                    if ans_len > right - left + 1:
                        ans_len = right - left + 1
                        ans_l, ans_r = left, right

                    left += 1

        if ans_len == float('inf'):
            return ""
        
        return s[ans_l: ans_r+1]

        # TC: O(m+n)
        # SC: O(distinct character)
        # Approach: increase count when freq becomes equal. While distinct char count is equal, move left

       




        