"""x = input('Введите число ')
def summa(x):
    if float(x) < 0:
        x = float(x) * (-1)
    number = 0
    for i in str(x):
        if i != '.':
            number += int(i)
    return number
print(f'Сумма чисел равна {summa(x)}')"""

n = input('Введите вещественное число: ')
sum = sum(map(int, n.replace('.', '')))
print (sum)