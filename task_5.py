import json
import os


def save_file(my_dict, file_name):
    with open(file_name, 'a+', encoding='utf-8') as f3:
        json.dump(my_dict, f3, ensure_ascii=False, indent=4)
        f3.write(',')


def test_save_to_file(file_name):
    with open(file_name, 'r', encoding='utf-8', errors='ignore') as f3:
        data_file = json.load(f3)
        print('\n'.join(map(str, data_file)))


def clear_file(f_name_x):
    with open(f_name_x, 'w', encoding='utf-8') as f3:
        f3.write('[')
        f3.close()


def Lost_line(f_name_x):
    with open(f_name_x, 'rb+') as fileh:
        fileh.seek(-1, os.SEEK_END)
        fileh.truncate()


def Lost_symbol(f_name_x):
    with open(f_name_x, 'a+', encoding='utf-8') as f5:
        f5.write(']')
        f5.close()


def task_5(f_name_1, f_name_2, f_name_3):
    clear_file(f_name_3)
    empty_list = {}
    with open(f_name_1, 'r+', encoding='utf-8') as f1:
        with open(f_name_2, 'r+', encoding='utf-8') as f2:
            while True:
                row_1 = f1.readline()
                row_2 = f2.readline()

                if not row_1:
                    Lost_line(f_name_3)
                    Lost_symbol(f_name_3)
                    test_save_to_file(f_name_3)
                    break

                else:
                    User_Name = row_1.splitlines()
                    User_Name = ' '.join(map(str, User_Name))
                    User_Name_2 = User_Name.split(',')
                    empty_list['Surname'] = User_Name_2[0]
                    empty_list['Name'] = User_Name_2[1]
                    empty_list['Lastname'] = User_Name_2[2]
                    Hobby_Name = row_2.splitlines()
                    Hobby_Name = ' '.join(map(str, Hobby_Name))
                    if Hobby_Name == '':
                        Hobby_Name = None
                    else:
                        Hobby_Name = Hobby_Name.split(',')
                    empty_list['Hobby'] = Hobby_Name
                    save_file(empty_list, f_name_3)


# task_5 ( 'users.csv', 'hobby.csv', 'result2.json' )

if __name__ == "__main__":
    var1 = input("Please enter path (full path+name_file.csv) to users: ")
    f_name_1 = str(var1)
    var2 = input("Please enter path (full path++name_file.csv) to hobby: ")
    f_name_2 = str(var2)
    var3 = input("Please enter path (full path++name_file.csv) to back_up: ")
    f_name_3 = str(var3)
    task_5(f_name_1, f_name_2, f_name_3)
