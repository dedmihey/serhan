def test(*par):
    print(par)
test('wir', [1, 2, 3], 25)

def fakt(m):
    if m == 1:
        return 1
    else:
        return m * fakt(m - 1)
k = int(input('Введите число и получите его факториал: '))
print(fakt(k))