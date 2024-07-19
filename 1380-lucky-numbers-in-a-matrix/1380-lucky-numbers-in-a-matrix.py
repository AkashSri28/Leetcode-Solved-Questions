class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # Step 1: Find the minimum element in each row
        min_in_rows = {min(row) for row in matrix}

        # Step 2: Find the maximum element in each column
        max_in_columns = {max(col) for col in zip(*matrix)}

        # Step 3: The intersection of min_in_rows and max_in_columns are the lucky numbers
        lucky_numbers = min_in_rows & max_in_columns

        return list(lucky_numbers)
        