class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i, j = len(a)-1, len(b)-1
        ans = []
        while i >= 0 or j >= 0 or carry > 0:
            a1 = int(a[i]) if i >= 0 else 0
            b1 = int(b[j]) if j >= 0 else 0
            s = a1+b1+carry
            match s:
                case 0:
                    ans.append("0")
                    carry = 0
                case 1:
                    ans.append("1")
                    carry = 0
                case 2:
                    ans.append("0")
                    carry = 1
                case 3:
                    ans.append("1")
                    carry = 1
                    
            i -= 1
            j -= 1
            
        
        return ''.join(ans)[::-1]
    
    # TC: O(max(len(a), len(b)))
    #     SC: O(max(len(a), len(b)))
    #         Approach: Start checking from right until we a bit/ carry is set. 
        