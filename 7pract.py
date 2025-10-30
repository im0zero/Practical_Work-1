#1.1
def s_ractangle():
    a = int(input("Введите значение 1 стороны: "))
    b = int(input("Введите значение 2 стороны: "))
    result = a * b
    print(f'Площадь прямоугольника = {result}')
s_ractangle()


def s_square():
    a = int(input("Введите значение стороны: "))
    result = a ** 2
    print(f'Площадь квадрата = {result}')
s_square()

def s_tringle():
    a = int(input("Введите значение основания: "))
    b = int(input("Введите значение высоты: "))
    result = (a * b) / 2
    print(f'площадь треугольника = {result}')
s_tringle()


#1.2
numbers1 = [2, 4, 3, 2, 1]
numbers2 = [5, 2, 3, 2, 1]
numbers3 = [1, 7, 3, 2, 1]
s1 = sum(numbers1)
averenge1 = s1 / len(numbers1)
s2 = sum(numbers2)
averenge2 = s2 / len(numbers2)
s3 = sum(numbers3)
averenge3 = s3 / len(numbers3)
print(f'Сумма массива(1) = {s1}\n Его среднее арифметическое = {averenge1} ')
print(f'Сумма массива(1) = {s2}\n Его среднее арифметическое = {averenge2} ')
print(f'Сумма массива(1) = {s3}\n Его среднее арифметическое = {averenge3} ')

#2.1
import math
def s_hexagon():
    a = float(input("Введите сторону шестиугоьника : "))
    result = (3 * math.sqrt(3) * a ** 2) / 2
    print(f'площадь правильного шестиугольника  = {result}')
s_hexagon()

#2.2
def s_three_rectangles():
    rectangles = 0
    for i in range(1,4):
        a = float(input("Введите длину: "))
        b = float(input("Введите ширину: "))
        rectangles += 1
        result = a * b
        print(f'Площадь прямоугольника номер: {rectangles} Равна = {result} ')
s_three_rectangles()

#9.1
numbers = int(input("Введите число: "))
a = 0
while numbers > 0:
    numbers -= sum(map(int, str(numbers)))
    a += 1
print(a)

#9.2
numbers1 = list(map(int, input("Введите 5 целых чисел через пробел: ").split()))
numbers2 = list(map(int, input("Введите 5 целых чисел через пробел: ").split()))
numbers3 = list(map(int, input("Введите 5 целых чисел через пробел: ").split()))
s1 = sum(numbers1)
averenge1 = s1 / len(numbers1)
s2 = sum(numbers2)
averenge2 = s2 / len(numbers2)
s3 = sum(numbers3)
averenge3 = s3 / len(numbers3)
print(f'Сумма массива(1) = {s1}\n Его среднее арифметическое = {averenge1} ')
print(f'Сумма массива(1) = {s2}\n Его среднее арифметическое = {averenge2} ')
print(f'Сумма массива(1) = {s3}\n Его среднее арифметическое = {averenge3} ')

