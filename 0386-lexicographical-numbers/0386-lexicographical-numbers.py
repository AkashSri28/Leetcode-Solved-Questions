class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def compare(x, y):
            if str(x) < str(y):
                return 1
            elif str(x) > str(y):
                return -1
            else:
                return 0
            
        ans = [i for i in range(1, n+1)]
        ans.sort(key=cmp_to_key(compare), reverse=True)
        return ans
            
        