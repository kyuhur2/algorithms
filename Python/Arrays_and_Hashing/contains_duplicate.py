from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) == len(nums)


if __name__ == "__main__":
    input_cases = [
        [],
        [1, 2, 3],
        [1, 2, 3, 3],
        [-1, -1],
    ]
    output_cases = [True, True, False, False]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        if solution.containsDuplicate(input_case) == output_case:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
