class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        heap = []
        for l, r in intervals:
            heap.append([l, 0])
            heap.append([r, 1])
            
        ans, cnt = 0, 0
        heap.sort()
        
        for i, flag in heap:
            if flag:
                cnt -= 1
            else:
                cnt += 1
            ans = max(ans, cnt)
            
        return ans
            
        