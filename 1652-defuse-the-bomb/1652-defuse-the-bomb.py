class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        temp = []
        
        for _ in range(3):
            for n in code:
                temp.append(n)
        
        n = len(code)
        for i in range(1, 3*n):
            temp[i] = temp[i-1]+temp[i]
            
        ans = []
        i, j = 0, 0
        if k > 0:
            i = n
            j = i+k
        elif k < 0:
            i = n + k - 1
            j = n - 1
        else:
            i = j = n
            
        for _ in range(n):
            res = temp[j] - temp[i]
            ans.append(res)
            i += 1
            j += 1
            
        return ans
            
            
        