class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeating = set()
        maxLength = 0
        left, right = 0, 0
        while right < len(s):
            while s[right] in repeating:
                repeating.remove(s[left])
                left += 1
            repeating.add(s[right])
            maxLength = max(maxLength, len(repeating))
            right += 1
        return maxLength


if __name__ == "__main__":
    input_cases = ["abcabcbb", "bbbbb", "pwwkew", ""]
    output_cases = [3, 1, 3, 0]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        if solution.lengthOfLongestSubstring(input_case) == output_case:
            print(f"Test {test_number}: Passed.")
        else:
            print(f"Test {test_number}: Failed.")
