from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            first = heapq.heappop(stones) * -1
            second = heapq.heappop(stones) * -1
            if first - second == 0:
                continue
            else:
                heapq.heappush(stones, -1 * (first - second))

        if len(stones) > 0:
            return stones[0] * -1
        else:
            return 0


if __name__ == "__main__":
    input_cases = [
        [2, 7, 4, 1, 8, 1],
        [1],
        [],
    ]
    output_cases = [1, 1, 0]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        if solution.lastStoneWeight(input_case) == output_case:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
