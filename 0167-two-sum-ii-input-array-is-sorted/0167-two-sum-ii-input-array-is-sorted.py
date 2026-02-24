class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        i, j = 0, n-1

        while True:
            curr = numbers[i] + numbers[j]
            if curr > target:
                j -= 1
            elif curr < target:
                i += 1
            else:
                return [i+1, j+1]

        # TC: O(n)
        # SC: O(1)
        # Approach: keep pointers on 2 ends, when you want to decrease sum, move right pointer, when you want to increase sum move left pointer


        