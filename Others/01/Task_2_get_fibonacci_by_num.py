# необходимо вычислить n-е число Фибоначчи при n ≥2

def fib(index):
    if index <= 0 or not isinstance(index, int):
        raise Exception('Введены некорректные данные')
    curr_index = 2
    prev_fib, curr_fib = 1, 1

    while index > curr_index:
        prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
        curr_index += 1
    return curr_fib if index != 1 else 1


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
