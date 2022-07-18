import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = collections.defaultdict(int)
        tDict = collections.defaultdict(int)
        for i in range(len(s)):
            sDict[s[i]] += 1
            tDict[t[i]] += 1

        return sDict == tDict

if __name__ == "__main__":
    input_cases = [
        ("", ""),
        ("abba", "bbaa"),
        ("abc", "abcd"),
        ("abc", "acd")
    ]
    expected_outputs = [
        True,
        True,
        False,
        False
    ]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, expected_outputs)):
        inputs, result = element
        input_1, input_2 = inputs
        if (solution.isAnagram(input_1, input_2) == result):
            print(f"Test {test_number}: Passed.")
        else:
            print(f"Test {test_number}: Failed.")
