# Задание 1
n = int(input('Введите длину массива: '))
m = int(input('Введите число M: '))
x = []
y = []

for i in range(n):
    element = int(input(f'Введите {i} элемент: '))
    x.append(element)

for element in x:
    if abs(element) > m:
        y.append(element)

print('Введённое число M:', m)
print('Массив X:', x)
print('Массив Y:', y)

# Задание 2
n = int(input('Введите длину массива: '))
a = []

for i in range(n):
    element = int(input(f'Введите {i} элемент: '))
    a.append(element)

print('Исходный массив:', a)

for i in range(len(a)):
    if a[i] < 0:
        a[i] = -a[i]

print('Полученный массив:', a)

# Задание 3
n = int(input('Введите количество элементов массива: '))
arr = []

for i in range(n):
    element = int(input(f'Введите {i} элемент: '))
    arr.append(element)

max_element = max(arr)
print('Максимальный элемент:', max_element)
print('Массив в обратном порядке:', arr[::-1])

# Задание 4
n = int(input('Введите количество элементов массива: '))
arr = []

for i in range(n):
    element = int(input(f'Введите {i} элемент: '))
    arr.append(element)

min_element = min(arr)
min_index = arr.index(min_element)
print('Минимальный элемент:', min_element)
print('Индекс минимального элемента:', min_index)

# Задание 5
n = 8
d = []
for i in range(n):
    element = int(input(f'Введите {i} элемент массива D: '))
    d.append(element)

sum_odd = 0
for i in range(len(d)):
    if i % 2 == 1:
        sum_odd += d[i]

print('Массив D:', d)
print('Сумма элементов с нечетными индексами:', sum_odd)

# Задание 9
n = int(input('Введите количество элементов массива: '))
arr = []

for i in range(n):
    element = float(input(f'Введите {i} элемент: '))
    arr.append(element)

min_abs_element = min(arr, key=abs)
print('Минимальный по модулю элемент:', min_abs_element)
print('Массив в обратном порядке:', arr[::-1])
