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
    test_cases = [
        ([1, 2, 3], 4, [0, 2]),
        ([1, 2, 3, 4], 7, [2, 3]),
        ([-1, 0, 5, -2], -3, [0, 3]),
        ([0, 1, 2, 3, 0], 0, [0, 4]),
    ]
    test = Solution()
    for input_1, input_2, result in test_cases:
        assert test.twoSum(input_1, input_2) == result

    print("All tests have passed.")
