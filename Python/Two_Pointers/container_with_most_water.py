from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVolume = 0
        left, right = 0, len(height) - 1
        while left < right:
            maxVolume = max(
                maxVolume, min(height[right], height[left]) * (right - left)
            )
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxVolume


if __name__ == "__main__":
    print("container_with_most_water")
    input_cases = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1], []]
    output_cases = [49, 1, 0]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        if solution.maxArea(input_case) == output_case:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
    print("\n")
