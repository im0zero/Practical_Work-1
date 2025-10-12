# Задание 1
n = int(input('Сколько чисел: '))
m = int(input('Число M: '))
x = []
y = []

i = 0
while i < n:
    num = int(input(f'Число {i}: '))
    x.append(num)
    i += 1

i = 0
while i < n:
    if abs(x[i]) > m:
        y.append(x[i])
    i += 1

print('M =', m)
print('X =', x)
print('Y =', y)

# Задание 2
n = int(input('Сколько чисел: '))
a = []

i = 0
while i < n:
    num = int(input(f'Число {i}: '))
    a.append(num)
    i += 1

print('Было:', a)

i = 0
while i < n:
    if a[i] < 0:
        a[i] = -a[i]
    i += 1

print('Стало:', a)

# Задание 3
n = int(input('Сколько чисел: '))
arr = []

i = 0
while i < n:
    num = int(input(f'Число {i}: '))
    arr.append(num)
    i += 1

max_num = arr[0]
i = 1
while i < n:
    if arr[i] > max_num:
        max_num = arr[i]
    i += 1

print('Самое большое:', max_num)
print('Наоборот:', arr[::-1])

# Задание 4
n = int(input('Сколько чисел: '))
arr = []

i = 0
while i < n:
    num = int(input(f'Число {i}: '))
    arr.append(num)
    i += 1

min_num = arr[0]
min_index = 0
i = 1
while i < n:
    if arr[i] < min_num:
        min_num = arr[i]
        min_index = i
    i += 1

print('Самое маленькое:', min_num)
print('Его номер:', min_index)

# Задание 5
d = []
i = 0
while i < 8:
    num = int(input(f'Число {i}: '))
    d.append(num)
    i += 1

s = 0
i = 1
while i < 8:
    s += d[i]
    i += 2

print('Массив D:', d)
print('Сумма нечетных:', s)

# Задание 9
n = int(input('Сколько чисел: '))
arr = []

i = 0
while i < n:
    num = float(input(f'Число {i}: '))
    arr.append(num)
    i += 1

min_abs = abs(arr[0])
i = 1
while i < n:
    if abs(arr[i]) < min_abs:
        min_abs = abs(arr[i])
    i += 1

print('Самое маленькое по модулю:', min_abs)
print('Наоборот:', arr[::-1])
