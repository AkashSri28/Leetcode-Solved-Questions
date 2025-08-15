class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = None
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if best is None or num[i] > best:  # char comparison works for digits
                    best = num[i]
        return "" if best is None else best * 3

        # TC: O(n)
        # SC: O(1)
        # Approach: From left to right, for each valid index check i, i+1, i+2. If they are same and greater than best. Update your best.






        
        