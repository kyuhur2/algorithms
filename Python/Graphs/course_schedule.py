from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = set()
        self.cycle = set()
        self.adjList = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            self.adjList[course].append(prereq)

        for course in range(numCourses):
            if not self.dfs(course):
                return False
        return True

    def dfs(self, course: int):
        if course in self.cycle:
            return False
        if course in self.visited:
            return True

        self.cycle.add(course)
        for prereq in self.adjList[course]:
            if not self.dfs(prereq):
                return False
        self.cycle.remove(course)
        self.visited.add(course)
        return True


if __name__ == "__main__":
    input_cases = [
        (2, [[1, 0]]),
        (2, [[1, 0], [0, 1]]),
        (6, [[1, 0], [5, 0], [4, 0], [5, 4], [4, 3], [3, 2], [4, 2], [2, 1]]),
    ]
    output_cases = [True, False, True]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        input_1, input_2 = input_case
        if solution.canFinish(input_1, input_2) == output_case:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
