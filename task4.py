src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
src2 = src[1:]
#print(src2)
#  Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего
# result = [12, 44, 4, 10, 78, 123]
result=[j for i, j in zip(src, src2) if j>i]
print(result)



