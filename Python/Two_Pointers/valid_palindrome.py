class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while end > start:
            if not s[start].isalnum():
                start += 1
                continue

            if not s[end].isalnum():
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True


if __name__ == "__main__":
    print("valid palindrome")
    input_cases = [
        "aba",
        "1",
        "",
        "12f12s",
        "41",
    ]
    expected_outputs = [True, True, True, False, False]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, expected_outputs)):
        input_case, expected_output = element
        if solution.isPalindrome(input_case) == expected_output:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
    print("\n")
