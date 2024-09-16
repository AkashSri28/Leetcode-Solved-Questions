class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_mins(tp):
            hr, mn = tp.split(":")
            return int(hr)*60+int(mn)
            
        time = [0]*(1440)
        
        for tp in timePoints:
            t = time_to_mins(tp)
            if time[t] == 1:
                return 0
            time[t] = 1
            
        ans = float('inf')
        first = curr = prev = None
        for i in range(1440):
            if time[i] == 1:
                if first == None:
                    first = i
                    curr = i
                else:
                    prev = curr
                    curr = i
                    ans = min(ans, abs(curr-prev))
                    
        # edge case
        ans = min(ans, (first-0)+(1440-curr))
        return ans
               
    #TC: O(n)   #traversing through timeList
    #SC: O(1440) or O(1)    #storing all possible time combinations
    #Approach: 1 approach is to sort and check time difference between adjacent values, but here possible values will be between 0 and 1439, so mark these values and check difference between adjacent values
    
                
        