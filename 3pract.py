#task1.2
print("Введите три целых числа:")
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

print("Числа из интервала [1,3]:")
if 1 <= a <= 3:
    print(a)
if 1 <= b <= 3:
    print(b)
if 1 <= c <= 3:
    print(c)

#task1.2
num = int(input("Введите двузначное число: "))
n1= num // 10
n2 = num % 10

if n1 == n2:
    print("Да")
else:
    print("Нет")

#task2.5
f = float(input("Введите f: "))
if f < 5:
    z = f + 2
elif f > 5:
    z = f - 1
else:
    z = 1
print("z =", z)


#task3.1
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if a > b:
    print("Наибольшее:", a)
elif b > a:
    print("Наибольшее:", b)
else:
    print("Числа равны")

#task3.2
a = int(input("Введите число: "))
if a % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")


#task3.5
a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))
result = (a + b + c) / 3

# Вывод результата
print("Среднее арифметическое:", result)
