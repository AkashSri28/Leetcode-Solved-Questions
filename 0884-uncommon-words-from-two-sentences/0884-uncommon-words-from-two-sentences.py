class Solution:
    def uncommonFromSentences(self, A, B):
        c = collections.Counter((A + " " + B).split())
        return [w for w in c if c[w] == 1]
#     def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
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
        