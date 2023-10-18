import numpy as n
# print('Создание массива из списка')
# a = n.array([1,2,3,4,5])
# print(a)
#
# print('Создание двумерного массива из списка списков')
# b = n.array([[1,2,3],[4,5,6], [7,8,9]])
# print(b)
#
# print('Создание массива из диапазона значений')
# c = n.arange(0,5,2)
# print(c)
#
# print('Создание массива из равномерно распределенных значений')
# f = n.linspace(0,1,5)
# print(f)
#
# print('Создание массива из случайных значений')
# e = n.random.rand(3, 3)
# print(e)
#
# print('Создание массива из нулей')
# h = n.zeros((2, 3))
# print(h)
#
# print('Создание массива из единиц')
# g = n.ones((4, 1))
# print(g)
import numpy.random

a = n.random.randint(1,10)
b = n.random.randint(1,10)
print('Mas a:/n', a)
print('Mas a:/n', b)

f = a + b
print('Cумма массива', b)

std_a = n.std(a)
print("Стандартное отклонение массива a:", std_a)

median_b = n.median(b)
print("Медиана массива b:", median_b)


min_b = n.min(b)
print("Минимальное значение массива b:", min_b)

max_a = n.max(a)
print("Максимальное значение массива a:", max_a)

sum_b = n.sum(b)
print("Сумма элементов массива b:", sum_b)


