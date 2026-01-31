class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        n = len(s)
        word_map = Counter(words)
        k = len(words)
        res = []

        for i in range(word_len):
            left = right = i
            seen = Counter()
            count = 0
            while right + word_len <= n:
                word = s[right:right+word_len]

                if word in word_map:
                    seen[word] += 1
                    count += 1

                    while seen[word] > word_map[word]:
                        seen_word = s[left: left+word_len]
                        seen[seen_word] -= 1
                        count -= 1
                        left += word_len

                    if count == k:
                        res.append(left)

                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    left = right + word_len
                    seen.clear()
                    count = 0

                right += word_len

        return res

        # TC: O(n)
        # SC: O(k)
        # Approach: find the window where all words in words exist. If invalid word is seen, move starting point of window
        