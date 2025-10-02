print("вариант 5:")
#вариант 5
text = "Маша гуляла в паркЕ"
print(text.lower())

print("вариант 9:")
#вариант 9
text = "мама мыла посуду, мама делала уборку"
print(text.count("мама"))

print("вариант 15:")
#вариант 15
text = "темно на улице,потому что уже вечер"
print(text.count("т"))

print("вариант 1:")
#вариант 1
text = "Ель растет в саду. Ее часто поливают"
count = 0
for word in text.split():
    if word[0].lower() == 'е':
        count +=1
print(count)

print("вариант 2:")
#вариант 2
text = "Пример : текст : здесь"
count = text.count(':')
print(text.replace(":", "%"))
print(count)

print('вариант 3:')
#вариант 3
text = "hello. wow."
print(text.replace('.', ''))

print('вариант 3:')
#вариант 4
text = 'Привет пока как дела'
count = text.count('а')
text = text.replace('а', "о")
print(count)
print(text)

print("вариант 7:")
#вариант 7
text = "папа пьет чай"
half = len(text) // 2
result = text[:half].replace('п', '*') + text[half:]
print(result)

print("вариант 10:")
#вариант 10
text = "hello world"
result = []
for word in text.split():
    result.append(word[0].upper() + word[1:].lower())
print(result)
