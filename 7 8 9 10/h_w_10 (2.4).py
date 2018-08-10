string = 'Leo Tolstoy*1828-08-28*1910-11-20'
parts = string.split('*')
##print(parts)

full_name = parts[0] + ','
##print (full_name)

born = parts[1].split('-')
##print(born)
born_year = int(born[0])
##print (born_year)

died = parts[2].split('-')
##print(died)
died_year = int(died[0])
##print(died_year)

age = died_year - born_year
##print(age)

print(full_name, age)
