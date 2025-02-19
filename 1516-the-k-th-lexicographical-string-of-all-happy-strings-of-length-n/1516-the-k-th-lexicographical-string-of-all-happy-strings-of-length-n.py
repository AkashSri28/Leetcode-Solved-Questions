class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        cnt = [0]

        def backtrack(index):
            nonlocal res
            if index == n:
                cnt[0] += 1
                if cnt[0] == k:
                    return True
                return False

            for ch in 'abc':
                if index > 0 and ch == res[index-1]:
                    continue
                res.append(ch)
                if backtrack(index+1):
                    return True
                res.pop()

            return False

        
        if backtrack(0):
            return ''.join(res)

        return ''
        