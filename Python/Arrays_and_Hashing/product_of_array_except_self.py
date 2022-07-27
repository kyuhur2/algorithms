from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = [1] * len(nums)
        back = [1] * len(nums)
        for i in range(1, len(nums)):
            front[i] = front[i - 1] * nums[i - 1]
            back[len(nums) - 1 - i] = back[len(nums) - i] * nums[len(nums) - i]

        return [i * j for i, j in zip(front, back)]


if __name__ == "__main__":
    input_cases = [[], [0], [0, 0], [1, 0], [1, 2, 3, 4], [-1, 1, 0, -3, 3]]
    output_cases = [[], [1], [0, 0], [0, 1], [24, 12, 8, 6], [0, 0, 9, 0, 0]]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        if solution.productExceptSelf(input_case) == output_case:
            print(f"Test {test_number}: Passed.")
        else:
            print(f"Test {test_number}: Failed.")
