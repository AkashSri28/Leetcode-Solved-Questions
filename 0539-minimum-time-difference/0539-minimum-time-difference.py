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
                    
                
        