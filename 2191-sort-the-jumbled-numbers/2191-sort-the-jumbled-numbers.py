class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        #function to convert each value to its mapped value
        def convert_mapped_value(num):
            nonlocal mapping
            list_num = list(str(num))
            for i in range(0, len(list_num)):
                list_num[i] = str(mapping[int(list_num[i])])
            return int(''.join(list_num))          
        
        #convert each value in nums to its mapping and store in dict
        mapped_dict = []
        for num in nums:
            mapped_value = convert_mapped_value(num)
            mapped_dict.append([num, mapped_value])
            
        # sorted_nums = [[num, mapped] for num, mapped in mapped_dict.items()]
        mapped_dict.sort(key = lambda x:x[1])
        return [num for num, mapped in mapped_dict]
            
        
        
        
        
# Approach: convert nums into its equivalent mapped values and put in dict
#     now sort dict by mapped values
#     return nums[0]
        