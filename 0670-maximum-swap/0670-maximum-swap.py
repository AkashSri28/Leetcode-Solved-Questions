class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        max_idx = len(num) - 1
        xi = yi = 0
        for i in range(len(num) - 1, -1, -1):
            if num[i] > num[max_idx]:
                max_idx = i
            elif num[i] < num[max_idx]:
                xi = i
                yi = max_idx
        num[xi], num[yi] = num[yi], num[xi]
        return int(''.join([str(x) for x in num]))
        
#         sorted_num = list(str(num))
#         # sorted_num = sorted(str_num)
#         # sorted_num.reverse()
        
#         i = len(sorted_num)-1
#         max_val = sorted_num[i]
#         max_index = i
#         while i >= 0:
#             if sorted_num[i] > max_val:
#                 max_val = sorted_num[i]
#                 max_index = i
#             i -= 1
            
#         j = 0
#         i = max_index
#         while j < i and sorted_num[j] >= sorted_num[i]:
#             j += 1
            
#         sorted_num[i], sorted_num[j] = sorted_num[j], sorted_num[i]
        
#         return int(''.join(sorted_num))
        