#result = [23, 1, 3, 10, 4, 11]
#Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов
# список с сохранением порядка их следования в исходном списке, например  :
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_dtls = set()
for dtl_s in src:  # O(n) * O(n) -> O(n ** 2)
    if src.count(dtl_s) == 1: # O(n)
        unique_dtls.add(dtl_s)
print([dtl_s for dtl_s in src if dtl_s in unique_dtls])
# __________БИНГО!!!!_________________________________________
#print([name for name in names if name in unique_names])