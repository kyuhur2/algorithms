from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> bool:
        freq = dict()
        for i, element in enumerate(nums):
            if element in freq:
                return [freq[element], i]
            else:
                freq[target - element] = i
        return -1

if __name__ == "__main__":
    input_cases = [
        ([1, 2, 3], 4),
        ([1, 2, 3, 4], 7),
        ([-1, 0, 5, -2], -3),
        ([0, 1, 2, 3, 0], 0),
    ]
    expected_outputs = [
        [0, 2],
        [2, 3],
        [0, 3],
        [0, 4]
    ]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, expected_outputs)):
        inputs, result = element
        input_1, input_2 = inputs
        if (solution.twoSum(input_1, input_2) == result):
            print(f"Test {test_number}: Passed.")
        else:
            print(f"Test {test_number}: Failed.")
