class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set()
        n = len(nums)
        res = []
        for num in nums:
            seen.add(num)

        def backtrack(index):
            if index == n:
                if ''.join(res) not in seen:
                    return True
                return False
            
            for ch in "01":
                res.append(ch)
                if backtrack(index+1):
                    return True
                res.pop()

            return False

        backtrack(0)

        return ''.join(res)

        