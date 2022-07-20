import functools


class Solution:
    @functools.lru_cache(maxsize=128)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == "__main__":
    input_cases = [2, 3, 5]
    expected_outputs = [2, 3, 8]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, expected_outputs)):
        input_case, expected_output = element
        if solution.climbStairs(input_case) == expected_output:
            print(f"Test {test_number}: Passed.")
        else:
            print(f"Test {test_number}: Failed.")
