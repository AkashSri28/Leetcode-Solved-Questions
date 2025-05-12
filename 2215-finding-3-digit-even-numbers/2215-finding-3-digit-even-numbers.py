class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        freq = [0]*10

        for num in digits:
            freq[num] += 1

        for i in range(100, 1000, 2):
            o = i
            temp = [0]*10
            a = i //100
            temp[a] += 1
            i %= 100
            b = i //10
            temp[b] += 1
            c = i % 10
            temp[c] += 1

            if (freq[a] >= temp[a] and freq[b] >= temp[b] and freq[c] >= temp[c]):
                res.append(o)

        return res