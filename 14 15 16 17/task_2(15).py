import math
def circles_intersect(x1, y1, r1, x2, y2, r2):
   circle_distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

   if (r1 + r2) >= circle_distance >= math.fabs(r1 - r2):
       print('Окружности пересекаются ')
       return True
   else:
       print('Окружности не пересекаются')
       return False

if circles_intersect(4, 4, 4, 2, 2, 1):
    print('Окружности пересекаются')
else:
    print('Окружности не пересекаются')