import unittest
from Task_1_Two_Sum import Solution

test_data = [
    [[2, 7, 11, 15], 9, [0, 1]],
    [[3, 11, 11, 15, 7, 2], 9, [4, 5]],
    [[3, 2, 4], 6, [1, 2]],
    [[3, 3], 6, [0, 1]],
]


class TestAddTwoNumbers(unittest.TestCase):
    def test_answers(self):
        for inp1, inp2, out in test_data:
            self.assertEqual(Solution.twoSum(inp1, inp2), out)
            self.assertEqual(type(Solution.twoSum(inp1, inp2)), list)
