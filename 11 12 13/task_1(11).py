import math
def degrees_2_radians(degrees):
    result = (degrees * math.pi)/180
    return result
result = degrees_2_radians(45)
print('Radians = %.2f' % result)
