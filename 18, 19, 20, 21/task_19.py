import random


def diff_min_max(num_limit, lower_bound, upper_bound):
    difference = 0
    max_num = lower_bound
    min_num = upper_bound
    for i in range(num_limit):
        x = random.randint(lower_bound, upper_bound)
        if x > max_num:
            max_num = x
        elif x < min_num:
            min_num = x

        difference = difference + (max_num - min_num)
    return difference


n = int(input('Введите количество чисел:'))
u = int(input('Введите первое число:'))
b = int(input('Введите последнее число:'))
if diff_min_max(n, u, b):
    print('Разница равна:', diff_min_max(n, u, b))
