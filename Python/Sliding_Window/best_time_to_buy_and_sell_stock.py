from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        maxValue = 0
        while right < len(prices) - 1:
            if prices[right] < prices[left]:
                left = right
            right += 1
            maxValue = max(maxValue, prices[right] - prices[left])
        return maxValue


if __name__ == "__main__":
    print("best_time_to_buy_and_sell_stock")
    input_cases = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1], [1, 2]]
    output_cases = [5, 0, 1]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        if solution.maxProfit(input_case) == output_case:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
    print("\n")
