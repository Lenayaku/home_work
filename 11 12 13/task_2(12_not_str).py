def sum_of_digits(number):
    hundred = number/100
    dozens = (number/10) % 10
    units = number % 10
    result = int(hundred) + int(dozens) + units
    return result


answer = sum_of_digits(325)
print('Amount is %d.' % answer)