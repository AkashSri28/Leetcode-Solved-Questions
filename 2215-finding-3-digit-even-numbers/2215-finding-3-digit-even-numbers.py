class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digit_count = Counter(digits)
        result = []

        for num in range(100, 1000):
            if num % 2 != 0:
                continue  # must be even

            d1, d2, d3 = map(int, str(num))
            num_count = Counter([d1, d2, d3])

            if all(num_count[d] <= digit_count[d] for d in num_count):
                result.append(num)

        return result
        