class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans = []
        ls = sorted(arr)
        rank = 1
        dic = {}
        for a in ls:
            if a not in dic:
                dic[a] = rank
                rank += 1
        
        for a in arr:
            ans.append(dic[a])
            
        return ans
    
    # TC: O(nlogn)
    #     O(nlogn) sorting + O(n) dic creation + O(n) ans generation
    # SC: O(n)
    #     O(n) dic + O(n) ls
    # Approach: we need to sort elements to find smallest number, smallest number will have rank 1. Increase rank everytime new number is seen
                
        