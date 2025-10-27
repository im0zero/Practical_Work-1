#1.1
N = int(input("Введите количество элементов массива: "))
arr = []
print("Введите элементы массива:")
for i in range(N):
    element = int(input(f"Элемент {i+1}: "))
    arr.append(element)

max_element = arr[0]
for element in arr:
    if element > max_element:
        max_element = element

print("Исходный массив:", arr)
print("Максимальный элемент:", max_element)
print("Массив в обратном порядке:", arr[::-1])

#1.2
numbers = list(map(float, input("Введите элементы массива через пробел: ").split()))
print("Исходный массив:", numbers)

average = sum(numbers) / len(numbers)

for i in range(len(numbers)):
    if numbers[i] == 0:
        numbers[i] = average

print("Среднее арифметическое:", average)
print("Массив после замены нулей:", numbers)


#2.1
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

min_element = min(arr)
min_index = arr.index(min_element)

print("Исходный массив:", arr)
print("Минимальный элемент:", min_element)
print("Индекс минимального элемента:", min_index)

#2.2
arr = list(map(int, input("Введите целые числа через пробел: ").split()))

positive_arr = []
other_arr = []

for number in arr:
    if number > 0:
        positive_arr.append(number)
    else:
        other_arr.append(number)

print("Исходный массив:", arr)
print("Массив положительных элементов:", positive_arr)
print("Массив остальных элементов:", other_arr)

#5.1
arr = list(map(int, input("Введите 10 чисел через пробел: ").split()))

print("Массив:", arr)
print("Пары отрицательных чисел:")

found = False
for i in range(len(arr) - 1):
    if arr[i] < 0 and arr[i+1] < 0:
        print(f"({arr[i]}, {arr[i+1]})")
        found = True

if not found:
    print("Таких пар нет")
#5.2
arr = list(map(int, input("Введите 10 целых чисел через пробел: ").split()))

print("Исходный массив:", arr)

new_arr = []
for num in arr:
    if num not in new_arr:
        new_arr.append(num)

print("Новый массив без повторяющихся элементов:", new_arr)
