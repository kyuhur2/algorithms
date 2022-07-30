from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, element in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while right > left:
                val = nums[left] + nums[right] + element
                if val > 0:
                    right -= 1
                elif val < 0:
                    left += 1
                else:
                    result.append([nums[left], nums[right], element])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return sorted([sorted(i) for i in result])


if __name__ == "__main__":
    input_cases = [[-1, 0, 1, 2, -1, -4], [0, 0, 0]]
    output_cases = [[[-1, -1, 2], [-1, 0, 1]], [[0, 0, 0]]]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        if solution.threeSum(input_case) == output_case:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
