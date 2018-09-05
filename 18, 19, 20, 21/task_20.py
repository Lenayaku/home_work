import random


def diff_even_odd(num_limit, lower_bound, upper_bound):
    sum_even = 0
    sum_odd = 0
    #diff = sum_even - sum_odd
    for i in range(num_limit):
        num = random.randint(lower_bound, upper_bound)
        if num % 2 == 0:
            sum_even = sum_even + num
        else:
            sum_odd = sum_odd + num
    return sum_even - sum_odd


print('Difference is', diff_even_odd(4, 0, 11))
