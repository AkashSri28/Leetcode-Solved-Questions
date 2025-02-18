class Solution:
    def smallestNumber(self, pattern: str) -> str:
        used = [False]*10
        curr = []

        def backtrack(index):
            if index == len(pattern):
                return True
            for i in range(1, 10):
                if used[i]:
                    continue
            
                if index == -1:
                    used[i] = True
                    curr.append(i)
                    if backtrack(index+1):
                        return True
                    used[i] = False
                    curr.pop()

                else:
                    ch = pattern[index]
                    if (ch == 'I' and i > curr[-1]) or (ch == 'D' and i < curr[-1]):
                        used[i] = True
                        curr.append(i)
                        if backtrack(index+1):
                            return True
                        used[i] = False
                        curr.pop()

            return False                    

        backtrack(-1)

        return ''.join(map(str, curr))

        