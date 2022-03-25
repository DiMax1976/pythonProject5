import json
import sys

f_name_1 = 'users.csv'  # Создадим исходные файлы
f_name_2 = 'hobby.csv'  # ____________________________________
f_name_3 = 'result.json'
empty_dict = {}


def save_file(my_dict, file_name):
    with open(file_name, 'w+', encoding='utf-8') as f3:
        print("Данные записаны в файл:", file_name)
        json.dump(my_dict, f3, ensure_ascii=False, indent=4)


def test_save_to_file(file_name):
    with open(f_name_3, 'r', encoding='utf-8') as f3:
        data_file = json.load(f3)
        print("Проверка записи, считано из файла:", f_name_3)
        print(type(data_file), data_file)


"""____________________________Создаю файлы_______________________________________"""
with open(f_name_1, 'w', encoding='utf-8') as f1:
    with open(f_name_2, 'w', encoding='utf-8') as f2:
        print("Иванов,Иван,Иванович", file=f1)
        print ( "Петров,Петр,Петрович", file=f1 )
        print("Путин,Владимир,Владимирович", file=f1)
        print("Байденко,Иосиф,Робертович", file=f1)
        print("скалолазание,охота", file=f2)
        print("горные лыжи", file=f2)
        print("Python", file=f2)
"""____________________Решаем основную задачу!____________________________________"""
with open(f_name_1, 'r+', encoding='utf-8') as f1:
    with open(f_name_2, 'r+', encoding='utf-8') as f2:

        while True:
            row_1 = f1.readline()
            row_2 = f2.readline()
            if not row_2:
                Hobby_Name = None
                tag = 0
            else:
                tag = 1
                Hobby_Name = row_2.splitlines()
                Hobby_Name = ' '.join(map(str, Hobby_Name))
            if not row_1:
                if tag == 1:
                    print("Создан словарь:")
                    print(empty_dict)
                    save_file(empty_dict, f_name_3)
                    test_save_to_file(f_name_3)
                    sys.exit(1)
                    break

                else:
                    print("Создан словарь:")
                    print(empty_dict)
                    break
            else:
                User_Name = row_1.splitlines()
                User_Name = ' '.join(map(str, User_Name))
                empty_dict[User_Name] = Hobby_Name
save_file(empty_dict, f_name_3)
test_save_to_file(f_name_3)
""""________________________________________________________________________________"""
