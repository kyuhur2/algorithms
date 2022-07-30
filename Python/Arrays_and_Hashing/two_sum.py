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
    output_cases = [[0, 2], [2, 3], [0, 3], [0, 4]]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        input_1, input_2 = input_case
        if solution.twoSum(input_1, input_2) == output_case:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
