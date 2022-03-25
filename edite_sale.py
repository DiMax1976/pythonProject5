import sys

def get_line(noms, file_name, New_data):
    with open('../lesson6/back_up.csv', 'w', encoding='utf-8') as f:
        f.close()  # Содание или очистка файл!
    with open(file_name, 'r+', encoding='utf-8') as f21, open('../lesson6/back_up.csv', 'a', encoding='utf-8') as f22:

        for i, line in enumerate(f21, 1):
            if i == noms:
                print(New_data, file=f22)  # Меняю строку
            else:
                f22.write(line)
    with open(file_name, 'w', encoding='utf-8') as f5:
        f5.close()  # Затираю файл - очистка
    tag = 0
    with open(file_name, 'a', encoding='utf-8') as f_3, open('../lesson6/back_up.csv', 'r+', encoding='utf-8') as f_4:
        for i, line in enumerate(f_4, 1):
            tag += 1
            f_3.write(line)  # перезаписываю файл
        if tag < noms:
            print("Всего -", tag, "записей в файле", "строки с номером", noms,
                  "не существует, уточните номер строки!")
            sys.exit(1)


if __name__ == "__main__":
    var1 = input("Введите номер записи:")
    noms_1 = int(var1)
    var2 = input("Введите новые данные о затратах:")
    noms_2 = str(var2)
    get_line(noms_1, '../lesson6/bakery.csv', noms_2)
