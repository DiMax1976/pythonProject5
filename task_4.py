import json
import os

f_name_1 = 'users.csv'  # Создадим исходные файлы
f_name_2 = 'hobby.csv'  # ____________________________________
f_name_3 = 'result2.json'

with open(f_name_3, 'w', encoding='utf-8') as f3:
    f3.write('[')
    f3.close()


def save_file(my_dict, file_name):
    with open(file_name, 'a+', encoding='utf-8') as f3:
        # print("Данные записаны в файл:", file_name)
        json.dump(my_dict, f3, ensure_ascii=False, indent=4)
        f3.write(',')


def test_save_to_file(file_name):
    with open(file_name, 'r', encoding='utf-8', errors='ignore') as f3:
        data_file = json.load(f3)
        # print ( "Проверка записи, считано из файла:", file_name )
        print('\n'.join(map(str, data_file)))


def Lost_line(f_name_x):
    with open(f_name_x, 'rb+') as fileh:
        fileh.seek(-1, os.SEEK_END)
        fileh.truncate()


def Lost_symbol(f_name_x):
    with open(f_name_x, 'a+', encoding='utf-8') as f5:
        f5.write(']')
        f5.close()


empty_list = {}
with open(f_name_1, 'r+', encoding='utf-8') as f1:
    with open(f_name_2, 'r+', encoding='utf-8') as f2:

        while True:
            row_1 = f1.readline()
            row_2 = f2.readline()

            if not row_1:
                # print ( "Создан словарь1:" )
                # save_file ( empty_list, f_name_3 )
                Lost_line(f_name_3)
                Lost_symbol(f_name_3)
                test_save_to_file(f_name_3)
                break

            else:
                # print ( "Создан словарь2:" )
                # print ( empty_list )
                User_Name = row_1.splitlines()
                User_Name = ' '.join(map(str, User_Name))
                User_Name_2 = User_Name.split(',')
                empty_list['Surname'] = User_Name_2[0]
                empty_list['Name'] = User_Name_2[1]
                empty_list['Lastname'] = User_Name_2[2]
                # print(Hobby_Name)
                Hobby_Name = row_2.splitlines()
                Hobby_Name = ' '.join(map(str, Hobby_Name))
                if Hobby_Name == '':
                    Hobby_Name = None
                else:
                    Hobby_Name = Hobby_Name.split(',')
                empty_list['Hobby'] = Hobby_Name
                save_file(empty_list, f_name_3)
