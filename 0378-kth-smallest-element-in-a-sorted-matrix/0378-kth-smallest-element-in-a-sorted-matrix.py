class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[n-1][n-1]
        ans = -1

        while low <= high:
            mid = (low + high)//2
            i, j = 0, n-1
            cnt = 0
            while i < n and j >= 0:
                c = matrix[i][j]
                if c <= mid:
                    cnt += j+1
                    i += 1
                else:
                    j -= 1
            if cnt >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans



        