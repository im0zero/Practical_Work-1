# Задача 1
a = int(input("Введите A: "))
b = int(input("Введите B: "))

print("Числа:")
i = a
while i <= b:
    print(i)
    i += 1

# Задача 2
a = int(input("Введите A: "))
b = int(input("Введите B: "))

print("Числа:")
if a < b:
    i = a
    while i <= b:
        print(i)
        i += 1
else:
    i = a
    while i >= b:
        print(i)
        i -= 1

# Задача 3
a = int(input("Введите A: "))
b = int(input("Введите B: "))

print("Нечетные числа:")
i = a
while i >= b:
    if i % 2 != 0:
        print(i)
    i -= 1

# Задача 4
n = int(input("Сколько чисел: "))
s = 0
count = 0

while count < n:
    num = int(input("Введите число: "))
    s += num
    count += 1

print("Сумма:", s)

# Задача 5
n = int(input("Введите n: "))
s = 0
i = 1

while i <= n:
    s += i * i * i
    i += 1

print("Сумма кубов:", s)

# Задача 6
n = int(input("Введите n: "))
f = 1
i = 1

while i <= n:
    f = f * i
    i += 1

print("Факториал:", f)

# Задача 7
n = int(input("Введите n: "))
sum_f = 0
f = 1
i = 1

while i <= n:
    f = f * i
    sum_f += f
    i += 1

print("Сумма факториалов:", sum_f)

# Задача 8
n = int(input("Введите n: "))
i = 1

while i <= n:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1

# Задача 9
n = int(input("Сколько чисел Фибоначчи: "))
a = 0
b = 1
s = 0
count = 0

while count < n:
    s += a
    a, b = b, a + b
    count += 1

print("Сумма:", s)

# Задача 10
n = int(input("Сколько чисел: "))
k = int(input("С какого номера: "))
a = 0
b = 1
s = 0
count = 0
current = 1

while current < k:
    a, b = b, a + b
    current += 1

while count < n:
    s += a
    a, b = b, a + b
    count += 1

print("Сумма:", s)
