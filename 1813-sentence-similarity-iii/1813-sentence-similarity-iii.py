class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        list_s1 = sentence1.split(" ")
        list_s2 = sentence2.split(" ")
        
        i = 0
        while i < min(len(list_s1), len(list_s2)) and list_s1[i] == list_s2[i]:
            i += 1
            
        j, k = len(list_s1)-1, len(list_s2)-1
        while j >= 0 and k >= 0 and list_s1[j] == list_s2[k]:
            j -= 1
            k -= 1
            
        if i > j or i > k:
            return True
        return False
        