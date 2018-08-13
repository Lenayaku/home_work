import math


def cone_square_and_volume(radius, height):

    square = math.pi * radius * (radius + math.sqrt(radius**2 + height**2))
    volume = 1/3 * math.pi * radius**2 * height
    return square, volume


result1, result2 = cone_square_and_volume(2, 10)
print('Square is %2.2f and Volume is %2.2f' % (result1, result2))


