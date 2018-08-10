snake_case = 'employee_first_name'
print(snake_case)
s2 = snake_case.split('_')
CamelCase = s2[0].title() + s2[1].title() + s2[2].title()
print(CamelCase)
