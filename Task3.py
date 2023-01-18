"""def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")
lst = []
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)"""

my_list = list(map(int, input('Введите числа, через пробел: ').split()))
print(sum(my_list[1::2]))

