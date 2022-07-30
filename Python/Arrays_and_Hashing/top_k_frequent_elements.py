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
    print("top_k_frequent_elements")
    input_cases = [([1, 1, 1, 2, 2, 3], 2), ([1], 1), ([], 0)]
    output_cases = [[1, 2], [1], []]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        input_1, input_2 = input_case
        if solution.topKFrequent(input_1, input_2) == output_case:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
    print("\n")
