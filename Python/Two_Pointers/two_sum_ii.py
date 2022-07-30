from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            currentValue = numbers[left] + numbers[right]
            if currentValue > target:
                right -= 1
            elif currentValue < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return [-1]


if __name__ == "__main__":
    print("two_sum_ii")
    input_cases = [
        ([0, 0, 0, 0, 0, 1, 2, 5, 5, 5, 5], 3),
        ([0, 1], 1),
        ([1, 2, 3], 5),
    ]
    expected_outputs = [[6, 7], [1, 2], [2, 3]]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, expected_outputs)):
        input_case, expected_output = element
        input_1, input_2 = input_case
        if solution.twoSum(input_1, input_2) == expected_output:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
    print("\n")
