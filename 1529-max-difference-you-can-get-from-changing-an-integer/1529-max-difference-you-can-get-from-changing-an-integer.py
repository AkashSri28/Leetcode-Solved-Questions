class Solution:
    def maxDiff(self, num: int) -> int:
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
        if arr[0] != 1:
            x = arr[0]
        else:
            for a in arr:
                if a > 1:
                    x = a
                    break

        mini= []

        for a in arr:
            if a == x:
                mini.append(0) if x != arr[0] else mini.append(1)
            else:
                mini.append(a)

        n = len(arr)
        ans = [0]*n
        c = 0

        for i in range(n-1, -1, -1):
            if maxi[i]-c >= mini[i]:
                ans[i] = maxi[i] - c - mini[i]
                c = 0
            else:
                ans[i] = maxi[i]*10 - c - mini[i]
                c = -1
        return int(''.join(map(str, ans)))

        # TC: O(d)
        # SC: O(d)
        # Approach: For max number, find first non 9 and update to 9. For min number, if first element is not 1, convert it to 1, else convert first non 0 or 1 number to 0


        