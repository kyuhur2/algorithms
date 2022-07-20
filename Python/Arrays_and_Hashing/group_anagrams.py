import collections
from typing import List


class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        freq = collections.defaultdict(list)
        for string in strings:
            freq["".join(sorted(string))].append(string)

        result = [sorted(i) for i in freq.values()]
        result.sort(key=lambda x: len(x))
        return result if result != [] else [[]]


if __name__ == "__main__":
    input_cases = [["eat", "tea", "tan", "ate", "nat", "bat"], [""], []]
    expected_outputs = [[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]], [[""]], [[]]]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, expected_outputs)):
        input_case, expected_output = element
        if solution.groupAnagrams(input_case) == expected_output:
            print(f"Test {test_number}: Passed.")
        else:
            print(f"Test {test_number}: Failed.")
