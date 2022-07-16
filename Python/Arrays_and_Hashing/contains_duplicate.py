from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) == len(nums)

if __name__ == "__main__":
    test_cases = [
        ([], True),
        ([1, 2, 3], True),
        ([1, 2, 3, 3], False),
        ([-1, -1], False),
    ]
    test = Solution()
    for input_1, result in test_cases:
        assert test.containsDuplicate(input_1) == result
        
    print("All tests have passed.")
