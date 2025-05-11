class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for num in arr:
            if num%2 == 1:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0
        return False

        # TC: O(n)
        # SC: O(1)
        # Approach: so we maintain a counter of odd number and return True if counter reaches 3. Reset the counter if even number is encountered


        