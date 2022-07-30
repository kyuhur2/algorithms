import functools


class Solution:
    @functools.lru_cache(maxsize=128)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == "__main__":
    print("climbing_stairs")
    input_cases = [2, 3, 5]
    output_cases = [2, 3, 8]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        if solution.climbStairs(input_case) == output_case:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
    print("\n")
