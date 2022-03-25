import sys


def save_money(*args):
    with open('../lesson6/bakery.csv', 'a', encoding='utf-8') as f1:
        for elem in args:
            print(elem, file=f1)


if __name__ == "__main__":
    full_argum = sys.argv
    arg_list = full_argum[1:]
    for my_money in arg_list:
        save_money(my_money)

