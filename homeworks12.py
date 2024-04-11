def print_params (a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2)
print_params(8, 'проза')
print_params(6.3, 7, 2)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [2, 'басня', True]
values_dict = {'a': 5, 'b': 'юмор', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [11, 'статья']
print_params(*values_list_2, 42)