from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = self.iterativeBinary(nums, 0, len(nums) - 1, target)
        return index

    def recursiveBinary(self, nums, left, right, target):
        mid = (right + left) // 2
        if left > right:
            return -1

        if nums[mid] < target:
            return self.recursiveBinary(nums, mid + 1, right, target)
        elif nums[mid] > target:
            return self.recursiveBinary(nums, left, mid - 1, target)
        else:
            return mid

    def iterativeBinary(self, nums, left, right, target):
        while right >= left:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    input_cases = [
        ([-1, 0, 3, 5, 9, 12], 9),
        ([-1, 0, 3, 5, 9, 12], 4),
        ([], 0),
        ([-20, -12, -10, -9, -7, -5], -7),
        ([-20, -12, -10, -9, -7, -5], -6),
    ]
    output_cases = [4, -1, -1, 4, -1]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        input_1, input_2 = input_case
        if solution.search(input_1, input_2) == output_case:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
