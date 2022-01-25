from typing import List

test_data = [
    [8, [2, 3, 0, 7, 9, 4, 8, 2]],
    [6, [0, 7, 9, 4, 8, 0]],
    [14, [0, 7, 9, 4, 8, 20, 0, 1, 2, 3, 0, 0, 0, 12]],
    [5, [0, 0, 0, 0, 0]],
    [1, [0]],
    [0, []],
    [2, ['Vl', 0]],
    ['vl', [1, 2]],
    [3, [1, 2]]
]


def find_index_to_zero(length: int, nums: List[int]) -> List[int]:
    if type(length) != int or length != len(nums) \
            or not nums or type(nums) != list:
        raise Exception('Введены некорректные данные')
    zeros_indexes = [index for index, val in enumerate(nums) if val == 0]
    answer = list()
    for n_index, n in enumerate(nums):
        if type(n) != int:
            raise Exception('Введены некорректные данные')
        elif n == 0:
            answer.append(0)
            continue

        diff = length
        for index_zero in zeros_indexes:
            current_diff = abs(n_index - index_zero)
            diff = diff if current_diff > diff else current_diff
        answer.append(diff)
    return answer


if __name__ == '__main__':
    inp_len = int(input('Введите длинну списка:'))
    inp_list_str = [int(n) for n in input('Введите список:').split()]
    print(find_index_to_zero(inp_len, inp_list_str))

    # for data in test_data:
    #     try:
    #         print(find_index_to_zero(data[0], data[1]))
    #     except Exception as e:
    #         print(e)
