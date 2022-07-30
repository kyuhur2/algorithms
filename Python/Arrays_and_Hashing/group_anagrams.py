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
    output_cases = [[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]], [[""]], [[]]]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        if solution.groupAnagrams(input_case) == output_case:
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
