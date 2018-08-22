def have_trains_crashed(v1, v2):
  time_1 = 4/v1
  time_2 = 6/v2
  if time_1 >= time_2:
      print('Столкновение произойдет.')
      return True
  else:
      print('Столкновение не произойдет.')
      return False
if have_trains_crashed(4, 6):
    print('Столкновение произойдет.')
else:
    print('Cтолкновение не произойдет.')