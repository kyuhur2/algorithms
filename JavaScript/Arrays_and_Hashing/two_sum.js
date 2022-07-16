import { isEqual, assert } from "../_lib/test.js";

var twoSum = function(nums, target) {
    let freq = {};
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] in freq) {
            return [freq[nums[i]], i];
        } else {
            freq[target - nums[i]] = i;
        };
    };
    return [-1]
};

var test_cases = [
    [[1, 2, 3, 4], 7, [2, 3]],
    [[-1, 2, 3], 1, [0, 1]],
    [[-1, 10, 1], 0, [0, 2]],
    [[-1, 12, 5, -1], -2, [0, 3]],
    [[0, 1, 2, 3, 0], 0, [0, 4]],
    [[], 0, [-1]]
];
for (let i = 0; i < test_cases.length; i++) {
    let result = test_cases[i];
    assert(
        isEqual(twoSum(result[0], result[1]), result[2]),
        i + 1
    );
};
