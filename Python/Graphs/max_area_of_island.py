from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        self.visited = set()
        self.grid = grid
        self.ROWS, self.COLS = len(grid), len(grid[0])
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    maxArea = max(self.dfs(i, j), maxArea)
        return maxArea

    def dfs(self, r, c):
        if (
            r < 0
            or r == self.ROWS
            or c < 0
            or c == self.COLS
            or self.grid[r][c] == 0
            or (r, c) in self.visited
        ):
            return 0

        self.visited.add((r, c))
        return (
            1
            + self.dfs(r + 1, c)
            + self.dfs(r - 1, c)
            + self.dfs(r, c + 1)
            + self.dfs(r, c - 1)
        )


if __name__ == "__main__":
    input_cases = [
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ],
        [[0], [0], [0], [0], [0]],
        [[0, 0, 0, 0, 0]],
        [[]],
    ]
    output_cases = [6, 0, 0, 0]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        if solution.maxAreaOfIsland(input_case) == output_case:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
