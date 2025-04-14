class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0

        for j in range(1, n - 1):
            valid_i = []
            valid_k = []

            # Collect valid i's
            for i in range(j):
                if abs(arr[i] - arr[j]) <= a:
                    valid_i.append(i)

            # Collect valid k's
            for k in range(j + 1, n):
                if abs(arr[k] - arr[j]) <= b:
                    valid_k.append(k)

            # Check final condition
            for i in valid_i:
                for k in valid_k:
                    if abs(arr[i] - arr[k]) <= c:
                        count += 1

        return count

        # cnt = 0
        # l = len(arr)
        # for i in range(l-2):
        #     for j in range(i+1, l-1):
        #         for k in range(j+1, l):
        #             if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
        #                 cnt += 1

        # return cnt
        