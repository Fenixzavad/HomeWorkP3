# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#     Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input("Введите число:  "))
list = []
for i in range(k+1):
    if i==0:
        list.append(i)
    elif i==1:
        list.append(i)
        list.insert(0, i)
    else:
        list.append(list[len(list)-1]+list[len(list)-2])
        list.insert(0, (-1)**(i-1)*list[len(list)-1])
print(list)