def process_data(input_filename, output_filename):
 

    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

            print(f"Прочитано строк: {len(lines)}")
            print("Содержимое файла:")
            for i, line in enumerate(lines, 1):
                print(f"{i}. {line.strip()}")

            results = []

            for line in lines:

                processed_line = line.strip().upper()
                results.append(processed_line)


        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for result in results:
                output_file.write(result + '\n')

        print(f"\nРезультаты успешно записаны в файл: {output_filename}")

    except FileNotFoundError:
        print(f"Ошибка: файл '{input_filename}' не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")



if __name__ == "__main__":
    input_file = "Каганер_АртемДенисович_УБ-52_vvod.txt"
    output_file = "Каганер_АртемДенисович_УБ-52_vivod.txt"


    with open(input_file, 'w', encoding='utf-8') as f:
        f.write("Первая строка\n")
        f.write("Вторая строка\n")
        f.write("Третья строка\n")

    print("Автор: Каганер Артем Денисович")
    print("Группа: УБ-52")
    print(f"Входной файл: {input_file}")
    print(f"Выходной файл: {output_file}")
    print("-" * 50)


    process_data(input_file, output_file)

