class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_list = defaultdict(int)
        s = s1+" "+s2
        for word in s.split(' '):
            word_list[word] += 1
            
        ans = []
        for key in word_list.keys():
            if word_list[key] == 1:
                ans.append(key)
                
        return ans
        
#         s1_set, s2_set = set(), set()
#         for word in s1.split(' '):
#             if word in s1_set:
#                 s2_set.add(word)
#             else:
#                 s1_set.add(word)
                
#         for word in s2.split(' '):
#             if word in s2_set:
#                 s1_set.add(word)
#             else:
#                 s2_set.add(word)
#         ans = s1_set.symmetric_difference(s2_set)
#         return ans


        
    #TC: O(len(s1)+len(s2))
    #SC: O(len(s1)+len(s2))
    #Approach: uncommon word is something which appears only once in both sentence, merge both sentence to form a single sentence and check if freq of any word is 1