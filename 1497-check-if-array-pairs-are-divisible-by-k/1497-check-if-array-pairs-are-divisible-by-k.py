class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        for i in range(n):
            arr[i] = arr[i]%k
            
        arr.sort()
        
        cnt = 0
        while cnt < n and arr[cnt] == 0:
            cnt += 1
        
        if cnt%2 != 0:
            return False
        
        j = n-1
        while cnt < j:
            if arr[cnt] + arr[j] != k:
                return False
            cnt += 1
            j -= 1
            
        return True
            
            
            
        