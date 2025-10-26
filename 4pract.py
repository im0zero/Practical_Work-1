#1
A = 10
B = 2
for num in range(A,B):
    num += 1
    print(num)
#2
A = int(input("Введите A: "))
B = int(input("Введите B: "))
if A > B:
    for num in range(B,A+1):
        print(num)
if A < B:
    for num in range(B,A-1,-1):
        print(num)
#3
A = int(input("Введите A: "))
B = int(input("Введите B: "))
i = A
while i >= B:
    if i % 2 != 0:
        print(i)
    i -= 1
#4
n = int(input("Введите количество: "))
sum = 0
count = 0

while count < n:
    num = int(input("Введите число: "))
    sum += num
    count += 1

print(f'Сумма чисел: {sum}')
print(f'Кол-во чисел: {count}')
#5
n = int(input('введите число: '))
f = 0
summ = 0
while n > 0:
    f += 1
    summ += f**3
    n -=1
print(f'Сумма равна {summ}')
