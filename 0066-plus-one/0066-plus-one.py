class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, ans, total = 1, [], 0
        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            if total >= 10:
                ans.append(0)
                carry = 1
            else:
                ans.append(total)
                carry = 0
        if carry == 1:
            ans.append(1)
        ans.reverse()
        return ans
        