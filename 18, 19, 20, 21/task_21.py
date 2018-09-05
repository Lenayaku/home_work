import random
def get_max_digit(number):
    max = 0
    for i in range(0, 12):
        n = int(number[i])
        if n > max:
            max = n
    return max


x = str(random.randint(100000000000, 999999999999))
s = get_max_digit(x)
print(x)
print("Max digit is", s)

