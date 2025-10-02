
# структура ветвления в Python
from operator import truediv

#print("Введите A:")
#A = input()
#print("Введите B:")
#B = input()
#if A==B:
#    print("A равно B")
#else:
#    print("A не равно B")


#a = int(input("Введите число:"))
#if a < 0:
#    print("a меньше нуля")
#elif a == 0:
#    print("a равно нулю")
#else:
#    print("a больше нуля")


#a = int(input("Введите число a:"))
#b = int(input("Введите число b:"))
#c = int(input("Введите число c:"))
#if a < b:
#    if a < c:
#        y = a
#else:
#    if b < c:
#        y = b
#        if b > c:
#            y = c
#print("наименьшее",y)


# task 1
#1.1
#a = int(input('введите число а '))
#b = int(input('введите число b '))
#c = int(input('введите число с '))
#if 1 <= a <= 3:
#    print('a',a)
#if 1 <= b <= 3:
#    print('b',b)
#if 1 <= c <= 3:
#    print('c',c)

#1.2
#number = input('Введите двухзначное число: ')
#if number[0] == number[1]:
#    print(number,' да, у числа одинаковые цифры')
#else:
#    print("Нет, у числа не одинаковые цифры")


#task 3
#1
#number_1 = int(input('Введите число '))
#number_2 = int(input('Введите число '))
#if number_1 > number_2:
#    print(number_1,'наибольшее число')
#else:
#    print(number_2,'наибольшее число')

#2
#number_1 = int(input('Введите число '))
#if number_1 % 2 == 0:
#    print(number_1,' число четное')
#else:
#    print('число нечетное')

#3
#number_1 = int(input('Введите число '))
#if number_1 % 2 == 0:
#    print(number_1,'четное число')
#else:
#    print(number_1,'нечетное число')


#4
#def is_prime_simple(n):
#    if n <= 1: # Числа меньше или равные 1 не являются простыми
#        return False
#    if n <= 3: # Числа 2 и 3 - простые
#        return True
#    if n % 2 == 0 or n % 3 == 0: # Все четные числа (кроме 2) и числа, делящиеся на 3 - составные
#        return False
#
#    i = 5
#    while i * i <= n: # Проверяем только до квадратного корня из n
#        if n % i == 0 or n % (i + 2) == 0: # Проверяем делимость на i и (i + 2)
#            return False
#        i += 6
#    return True
#print(is_prime_simple())

def truncate(text, length):
    if len(text) <= length:
        return text
    return text[:length] + '...'

print(truncate("hexlet", 2))




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
