class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for row in grid:
            for num in row:
                arr.append(num)

        arr.sort()
        mid = len(arr)//2

        target = arr[mid]

        op = 0 
        for num in arr:
            diff = abs(target - num)
            if diff % x != 0:
                return -1
            op += (diff//x)

        return op
        