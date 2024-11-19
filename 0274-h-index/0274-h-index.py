class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for index, c in enumerate(citations):
            if c >= index+1:
                h_index = index+1
        return h_index
        