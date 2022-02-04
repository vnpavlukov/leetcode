from typing import List


def find_index_to_zero(length: int, nums: List[int]) -> List[int]:
    if type(length) != int or type(nums) != list:
        raise TypeError('Введен некорректный тип данных')
    elif not nums:
        raise ValueError('Введены некорректные данные')
    zeros_indexes = [index for index, val in enumerate(nums) if val == 0]
    answer = list()
    for n_index, n in enumerate(nums):
        if type(n) != int:
            raise TypeError('Введен некорректный тип данных')
        elif length != len(nums):
            raise ValueError('Введены некорректные данные')
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
