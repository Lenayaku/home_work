def sum_of_digits(number):
    number = str(number)
    hundreds = int(number[:1])
    dozens = int(number[1:2])
    units = int(number[2:])
    result = hundreds + dozens + units
    return result


answer = sum_of_digits(325)
print('Amount is %d' % answer)



