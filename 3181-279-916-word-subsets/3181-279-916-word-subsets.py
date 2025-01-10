class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def checkSubset(count_a, count_b):
            for cb in count_b:
                if count_b[cb] > count_a.get(cb, 0):
                    return False
            return True

        res = []
        count_b = defaultdict(int)
        for w2 in words2:
            count = Counter(w2)
            for ch, cnt in count.items():
                count_b[ch] = max(cnt, count_b[ch])
            
        for w1 in words1:
            count_a = Counter(w1)
            if checkSubset(count_a, count_b):
                res.append(w1)

        return res

        # TC: O(m*len(words2) + n*len(words1))
        # SC: O(26)
        # Approach: Since we need to find words which contain all subsets from words2, we can combine words from words2 and then check words1
        