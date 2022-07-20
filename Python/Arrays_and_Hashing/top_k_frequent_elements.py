import heapq
import collections

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        array = [[-1 * value, key] for key, value in freq.items()]
        heapq.heapify(array)

        result = []
        for _ in range(k):
            _, key = heapq.heappop(array)
            result.append(key)
        return result


if __name__ == "__main__":
    input_cases = [([1, 1, 1, 2, 2, 3], 2), ([1], 1), ([], 0)]
    expected_outputs = [[1, 2], [1], []]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, expected_outputs)):
        input_case, expected_output = element
        input_1, input_2 = input_case
        if solution.topKFrequent(input_1, input_2) == expected_output:
            print(f"Test {test_number}: Passed.")
        else:
            print(f"Test {test_number}: Failed.")