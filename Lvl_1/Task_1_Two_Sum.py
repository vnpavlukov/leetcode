from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        for index_check in range(len(nums) - 1):
            for iterations in range(len(nums) - index_check - 1):
                if nums[index_check] + nums[index_check + iterations + 1] == target:
                    return [index_check, index_check + iterations + 1]


test_data = [
    [[2, 7, 11, 15], 9],
    [[3, 11, 11, 15, 7, 2], 9],
    [[3, 2, 4], 6],
    [[3, 3], 6],
]

for data in test_data:
    print(Solution().twoSum(data[0], data[1]))
