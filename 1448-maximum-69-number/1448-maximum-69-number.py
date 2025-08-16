class Solution:
    def maximum69Number (self, num: int) -> int:
        s_num = list(str(num))   # make it a list
        for i in range(len(s_num)):
            if s_num[i] == '6':
                s_num[i] = '9'
                break
        return int(''.join(s_num))


        