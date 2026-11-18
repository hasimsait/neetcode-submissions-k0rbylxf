class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        from collections import defaultdict

        for r in range(rows):
            for c in range(1, cols):
                matrix[r][c] += matrix[r][c - 1]

        ans = 0
        for c1 in range(cols):
            for c2 in range(c1, cols):
                prefix_counts = defaultdict(int)
                prefix_counts[0] = 1
                curr_sum = 0

                for r in range(rows):
                    row_slice_sum = matrix[r][c2] - (matrix[r][c1 - 1] if c1 > 0 else 0)
                    curr_sum += row_slice_sum
                    ans += prefix_counts[curr_sum - target]
                    prefix_counts[curr_sum] += 1

        return ans