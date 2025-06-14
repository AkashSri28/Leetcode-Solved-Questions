class Solution:
    def minMaxDifference(self, num: int) -> int:
        arr = [int(d) for d in str(num)]
        x = -1
        for a in arr:
            if a != 9:
                x = a
                break

        maxi = []
        for a in arr:
            if a == x:
                maxi.append(9)
            else:
                maxi.append(a)

        x = -1
        for a in arr:
            if a != 0:
                x = a
                break

        mini = []
        for a in arr:
            if a == x:
                mini.append(0)
            else:
                mini.append(a)

        return int(''.join(map(str, maxi))) - int(''.join(map(str, mini)))



        