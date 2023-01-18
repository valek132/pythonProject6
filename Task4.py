mass = [2, 3, 4, 5, 6]
mass2=[]
for i in range(len(mass)//2+len(mass)%2):
    mass2.append(mass[i]*mass[len(mass)-1-i])
print(mass2)

"""
import math
list_a = list(map(int, input('Введите числа, через пробел: ').split()))
print('Исходный список: ',list_a)
print('Результат: ',list([a*b for a,b in zip(list_a[0:math.ceil(len(list_a)/2)],list_a[::-1])]))"""