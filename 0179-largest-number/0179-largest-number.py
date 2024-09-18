class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 9,97,956
        # 9,97,956
        def compare(x, y):
            if x+y > y+x:
                return -1
            elif x+y < y+x:
                return 1
            else:
                return 0
        
        temp = [str(n) for n in nums]
        temp.sort(key=cmp_to_key(compare))
        
        if temp[0] == '0':
            return '0'
        
        return ''.join(temp)
        