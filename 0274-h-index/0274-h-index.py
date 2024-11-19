class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for index, c in enumerate(citations):
            if c >= index+1:
                h_index = index+1
        return h_index
    
    # TC: O(nlogn)
    #     SC: O(1)
    #         Approach: paper count is index+1, we try to increase paper count to the point where c is just greater than or equal to paper count. We could have used binary search here as well.
        