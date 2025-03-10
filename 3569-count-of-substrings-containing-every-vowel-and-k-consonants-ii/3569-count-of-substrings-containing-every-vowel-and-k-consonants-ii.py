class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleastk(k):
            mem = defaultdict(int)
            cnt = 0
            ans = 0
            l = 0
            for r in range(len(word)):
                if word[r] in 'aeiou':
                    mem[word[r]] += 1
                else:
                    cnt += 1

                while len(mem) == 5 and cnt >= k:
                    ans += (len(word) - r)
                    if word[l] in "aeiou":
                        mem[word[l]] -= 1
                        if mem[word[l]] == 0:
                            mem.pop(word[l])
                    else:
                        cnt -= 1
                    l += 1

            return ans

        return atleastk(k) - atleastk(k+1)

            


        