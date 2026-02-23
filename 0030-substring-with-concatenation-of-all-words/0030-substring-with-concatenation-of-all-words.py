class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words)
        word_len = len(words[0])
        ans = []
        words_freq = Counter(words)

        for i in range(word_len):
            left = right = i
            cnt = 0
            mem = defaultdict(int)

            while right + word_len <= len(s):
                word = s[right: right+word_len]
                if word in words_freq:
                    cnt += 1
                    mem[word] += 1

                    while mem[word] > words_freq[word]:
                        left_word = s[left: left+word_len]
                        mem[left_word] -= 1
                        cnt -= 1
                        left += word_len

                    if cnt == n:
                        ans.append(left)

                    print(mem, left)

                else:
                    left = right + word_len
                    mem.clear()
                    cnt = 0
                right += word_len

        return ans

        # TC: O(N*L)
        # SC: O(M*L)
        # Approach: For all possible start points, check number of consecutive words which satisfy condition. If word count get high then remove from left. If invalid word occurs, reset map and shift left


                





        