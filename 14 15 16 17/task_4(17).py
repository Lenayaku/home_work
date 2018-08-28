import math


def solve_quadratic_equation(a, b, c):
    discriminant = ((b**2) - (4 * a * c))
    print('Дискриминант равен %.2f.' % discriminant)
    if discriminant > 0:
        x1 = ((-b) + math.sqrt(discriminant)) / (2 * a)
        x2 = ((-b) - math.sqrt(discriminant)) / (2 * a)
        print('Первый корень равен %.2f, а второй %.2f.' % (x1, x2))
        return x1, x2
    elif discriminant == 0:
        x1 = ((-b) + math.sqrt(discriminant)) / (2 * a)
        print('Корень равен %.2f.' % x1)
        return x1, None
    else:
        print('Уравнение не имеет корней.')
        return None, None


a1 = int(input('Введите a:'))
b1 = int(input('Введите b:'))
c1 = int(input('Введите c:'))

if solve_quadratic_equation(a1, b1, c1):
    print('Результат: ', solve_quadratic_equation(a1, b1, c1))








