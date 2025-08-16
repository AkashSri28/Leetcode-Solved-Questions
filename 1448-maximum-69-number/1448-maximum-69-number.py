class Solution:
    def maximum69Number (self, num: int) -> int:
        # s_num = list(str(num))   # make it a list
        # for i in range(len(s_num)):
        #     if s_num[i] == '6':
        #         s_num[i] = '9'
        #         break
        # return int(''.join(s_num))
        return int(str(num).replace("6", "9", 1))

        # TC: O(d)
        # SC: O(d)
        # Approach: Check from left to right and replace first 9 with 6


        