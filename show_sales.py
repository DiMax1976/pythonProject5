import sys


def None_param():
    with open('../lesson6/bakery.csv', 'r', encoding='utf-8') as f_1:
        while True:
            row_1 = f_1.readline()
            print(row_1, end='')
            if not row_1:
                break


def one_param(row_2):
    with open('../lesson6/bakery.csv', 'r', encoding='utf-8') as f_2:
        row_2_1 = f_2.readlines()
    row_lines = ''.join(row_2_1[int(row_2) - 1:])
    print(row_lines)


def two_param(row_3, row_4):
    with open('../lesson6/bakery.csv', 'r', encoding='utf-8') as f_2:
        row_2_1 = f_2.readlines()
    row_lines = ''.join(row_2_1[int(row_3) - 1:int(row_4)])
    print(row_lines)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            two_param(sys.argv[1], sys.argv[2])
        else:
            one_param(sys.argv[1])
    else:
        None_param()
