# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
#     Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
list_count = []
for i in range(len(list)):
    if list[i] % 1 != 0:
        list_count.append(list[i])
list_count1 = [round(list_count[i] % 1, 2) for i in range(len(list_count))]
print(f"{list_count1} => {max(list_count1) - min(list_count1)}")