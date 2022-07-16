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
    test_cases = [
        ("", "", True),
        ("abba", "bbaa", True),
        ("abc", "abcd", False),
        ("abc", "acd", False),
    ]
    test = Solution()
    for input_1, input_2, result in test_cases:
        assert test.isAnagram(input_1, input_2) == result
        
    print("All tests have passed.")
