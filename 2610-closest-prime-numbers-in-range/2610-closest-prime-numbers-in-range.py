class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        mem = [True]*(right+1)
        for i in range(0, int(sqrt(right))+1):
            if i < 2:
                mem[i] = False
            if not mem[i]:
                continue
            j = 2
            while i*j <= right:
                mem[i*j] = False
                j += 1

        ans = [-1, -1]
        diff = right - left + 1
        primes = []
        for i in range(left, len(mem)):
            if mem[i]:
                primes.append(i)

        for i in range(len(primes)-1):
            if diff > primes[i+1] - primes[i]:
                diff = primes[i+1] - primes[i]
                ans = [primes[i], primes[i+1]]

        return ans

        # TC: O(nloglogn)
        # SC: O(n)
        # Approach: Using Sieve method to find prime numbers. TC of Sieve is O(nloglogn)






        