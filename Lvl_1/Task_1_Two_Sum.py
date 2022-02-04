from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        for index_check in range(len(nums) - 1):
            for iterations in range(len(nums) - index_check - 1):
                if nums[index_check] + nums[index_check + iterations + 1] == target:
                    return [index_check, index_check + iterations + 1]
