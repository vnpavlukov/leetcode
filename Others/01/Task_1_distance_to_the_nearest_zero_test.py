import unittest
from Task_1_distance_to_the_nearest_zero import find_index_to_zero

check_data = [
    [8, [2, 3, 0, 7, 9, 4, 8, 2], [2, 1, 0, 1, 2, 3, 4, 5]],
    [6, [0, 7, 9, 4, 8, 0], [0, 1, 2, 2, 1, 0]],
    [
        14, [0, 7, 9, 4, 8, 20, 0, 1, 2, 3, 0, 0, 0, 12],
        [0, 1, 2, 3, 2, 1, 0, 1, 2, 1, 0, 0, 0, 1]
     ],
    [5, [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
    [1, [0], [0]],
    ]

value_error_data = [
    [3, [1, 2]],
    [1, []],
]

type_error_data = [
    [2, ['Vl', 0]],
    ['vl', [1, 2]],
    [1, 'vl'],
]


class TestAddTwoNumbers(unittest.TestCase):
    def test_current_answers(self):
        for inp1, inp2, out in check_data:
            self.assertEqual(find_index_to_zero(inp1, inp2), out)
            self.assertEqual(type(find_index_to_zero(inp1, inp2)), list)

    def test_value_error(self):
        for data in value_error_data:
            self.assertRaises(ValueError, find_index_to_zero, data[0], data[1])

    def type_error_data(self):
        for data in value_error_data:
            self.assertRaises(ValueError, find_index_to_zero, data[0], data[1])
