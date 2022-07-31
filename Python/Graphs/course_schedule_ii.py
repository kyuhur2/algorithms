from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.visited = set()
        self.cycle = set()
        self.result = []
        self.adjList = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            self.adjList[course].append(prereq)

        for course in range(numCourses):
            if not self.dfs(course):
                return []
        return self.result
    
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
        self.result.append(course)
        return True


if __name__ == "__main__":
    input_cases = [
        (2, [[1, 0]]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
        (1, []),
    ]
    output_cases = [[0, 1], [0, 1, 2, 3], [0]]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        input_1, input_2 = input_case
        if solution.findOrder(input_1, input_2) == output_case:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
