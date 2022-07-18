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
    expected_outputs = [
        True,
        True,
        False,
        False
    ]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, expected_outputs)):
        input_case, expected_output = element
        if (solution.containsDuplicate(input_case) == expected_output):
            print(f"Test {test_number}: Passed.")
        else:
            print(f"Test {test_number}: Failed.")
