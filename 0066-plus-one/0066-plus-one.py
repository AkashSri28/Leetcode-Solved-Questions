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
    
    # TC: O(n)
    #     SC:O(n)
    #         Approach: we will iterate on all numbers from reverse order, and keep adding carry where required. Now if digit becomes 10, we need to set carry for next digit. If carry is left after iteration, add carry as last element
        
