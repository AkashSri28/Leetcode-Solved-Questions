class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for i in range(len(words)):
            if words[i][0] != words[i-1][-1]:
                return False
            
        return True
    
    # TC: O(n)    n: list of words
    #         SC: O(n)
    #             Approach: for all consecutive words, compare last and first char of adjacent words. At last, check first and last
        