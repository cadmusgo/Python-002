"""
作业二：
自定义一个 python 函数，实现 map() 函数的功能。
"""


def my_map(func, num):
    i = 0
    new_list = list(range(len(num)))
    for n in num:
        new_list[i] = func(n)
        i = i + 1

    return new_list


def calc_double(n):
    return 2 * n


def run():
    print(my_map(calc_double, [1, 2, 3, 4, 5]))


if __name__ == "__main__":
    run()
