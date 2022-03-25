tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Кира', 'Найтли', 'Ильгиз']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def klasses_a(my_list):
    for y in my_list:
        yield (y)


klas = klasses_a(klasses)
for x in tutors:
    try:
        tupl_s = (x, next(klas))
        print(tupl_s)
    except StopIteration:
        tupl_s = (x, None)
        print(tupl_s)

# "Гусь" то оказался не   такой сложный )))) Как поначалу показалось!!!