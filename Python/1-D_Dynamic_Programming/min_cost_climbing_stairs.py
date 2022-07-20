from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if cost == []:
            return -1

        if len(cost) == 1:
            return cost[0]

        dp = [0] * (len(cost) + 2)
        for i in reversed(range(len(cost))):
            dp[i] = min(cost[i] + dp[i + 2], cost[i] + dp[i + 1])
        return min(dp[0], dp[1])


if __name__ == "__main__":
    input_cases = [[], [1], [10, 15, 20], [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]]
    expected_outputs = [-1, 1, 15, 6]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, expected_outputs)):
        input_case, expected_output = element
        if solution.minCostClimbingStairs(input_case) == expected_output:
            print(f"Test {test_number}: Passed.")
        else:
            print(f"Test {test_number}: Failed.")
