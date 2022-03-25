
unique_ip={}
with open('../lesson6/nginx_logs.txt', 'r', encoding='utf-8') as file_1, \
    open('../lesson6/result_logs.txt', 'w', encoding='utf-8') as file_2:# Дополнительно сохранить в файл! Может и пригодится - хотя в задании нету такого
    cont_f=file_1.readlines()
    cont_f_2 = file_1.read()
    for row in cont_f:
        empty_tuple = ()
        frequency = {}
        IP_Num=(row.split(' - - ')[0])
        if IP_Num not in unique_ip:
            unique_ip[IP_Num]=1
        else:
            unique_ip[IP_Num]+=1
        IP_Num_2 = (row.split('] "')[1])
        IP_Num_3 = (IP_Num_2.split(' HTTP')[0])
        IP_Num_4 = (IP_Num_3.split(' ')[0])
        IP_Num_5 = (IP_Num_3.split(' ')[1])
        empty_tuple = (IP_Num, IP_Num_4, IP_Num_5)

        print(empty_tuple, )
        print(IP_Num, IP_Num_4, IP_Num_5, file=file_2)# Дополнительно сохранить в файл! Может и пригодится - хотя в задании нету такого
#___________Ищем спамера_______________________________________________
max_ip=max(unique_ip.values())
final_dict = {k: v for k, v in unique_ip.items() if v == max_ip}
for key, value in final_dict.items():
    print("Спамер найден на IP", key, "Он обращался - ", value, " раз")
