class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_dict = defaultdict(int)
        
        for i in nums:
            freq_dict[i] += 1
        
        res = []
        freq_list = [[k,v] for k, v in freq_dict.items()]
        freq_list.sort(key= lambda x: (x[1], -x[0]))
        
        for num, freq in freq_list:
            while freq > 0:
                res.append(num)
                freq -= 1
        
        return res
            
# TC: O(nlogn)
#     O(n)    create dict
#     O(n)    create freq_list
#     O(nlogn)    sort freq_list
#     O(n)    create res
# SC: O(n)
#     O(n)    create dict
#     O(n)    create freq_list
#     O(n)    res
    
# Approach: store all elements and its freq in dictionary,
#     now convert dictionary to 2d list
#     sort 2d list
#     now based on freq create res array