import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        numOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in self.visited:
                    self.iterativeDFS(grid, i, j)
                    numOfIslands += 1
        return numOfIslands

    def recursiveDFS(self, grid, r, c):
        if (
            r < 0
            or r >= len(grid)
            or c < 0
            or c >= len(grid[0])
            or grid[r][c] == "0"
            or (r, c) in self.visited
        ):
            return

        self.visited.add((r, c))
        for nr, nc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nr, nc = r + nr, c + nc
            self.recursiveDFS(grid, nr, nc)

    def iterativeDFS(self, grid, r, c):
        q = collections.deque([(r, c)])
        while q:
            r, c = q.popleft()
            if (
                r < 0
                or r >= len(grid)
                or c < 0
                or c >= len(grid[0])
                or grid[r][c] == "0"
                or (r, c) in self.visited
            ):
                continue

            self.visited.add((r, c))
            for nr, nc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                nr, nc = r + nr, c + nc
                q.append((nr, nc))


if __name__ == "__main__":
    input_cases = [
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        [],
    ]
    output_cases = [1, 3, 0]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        if solution.numIslands(input_case) == output_case:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
