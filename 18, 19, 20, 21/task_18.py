def sum_symbol_codes(first, last):
    codes_sum = 0
    symbol_top = ord(first)
    symbol_bottom = ord(last) + 1
    for i in range(symbol_top, symbol_bottom):
        codes_sum = codes_sum + i
    return codes_sum

print('Total sum:', sum_symbol_codes('a', 'z'))
