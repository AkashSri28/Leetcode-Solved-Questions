class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key = lambda x: x[0])
        i = 0
        while i < len(intervals):
            j = i + 1
            curr = intervals[i]
            while j < len(intervals) and curr[1] >= intervals[j][0]:
                curr[1] = max(curr[1], intervals[j][1])
                j += 1 

            ans.append(curr)
            i = j

        return ans
        