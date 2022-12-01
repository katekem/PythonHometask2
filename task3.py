# Реализуйте алгоритм перемешивания списка. 
# Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

# Решение ниже разбирали в среду, под ним оставила свои попытки (закомментила)
# Их конечно проверять не надо)

from random import randint as Ri
my_list = [Ri(0,100) for _ in range(10)]
print(my_list)
new_list = my_list[:]
while True:
    for i in range(len(my_list)):
        k = Ri(0,len(my_list)-1)
        new_list[i], new_list[k] = new_list[k], new_list[i]
    for i in range(len(my_list)):
        if new_list[i] == my_list[i]:
            print('Нашлось повторение')
            break
    else:
        break
print(new_list)



# import random as rnd
# r = rnd.randint(0,5)
# rnd_range = []
# for i in range(5):
#     if r not in rnd_range:
#         rnd_range.append(r)
#         r = rnd.randint(0,5)
#     else:
#         r = rnd.randint(0,5)
# print(rnd_range)


# n = int(input('Введите размер списка: '))
# my_list = [rnd.randint(0,40) for x in range(n)]
# print(my_list)

# rnd_list = []
# for e in range(len(my_list)):
#     rnd_list.append(None)
# print(rnd_list)
# r = rnd.randint(0,n-1)
# for i in range(len(my_list)):
#     if rnd_list[r] == None:
#         rnd_list[r] = (my_list[i])
#         print(rnd_list)
#     else:
#         r = rnd.randint(0,n-1)
#         i -= 1

#     rnd_list.append(my_list[r])
#     print(rnd_list)
#     rstart += 1
#     r = rnd.randint(rstart,n-1)
#     print(f'rstart = {rstart}, r = {r}')
#     print()
    

# r = rnd.randint(0,n)
# for e in range(len(rnd_list)):
#     if my_list[r] in rnd_list:
#         print(f'r = {r} exists')
#         r = rnd.randint(0,n)
#     else:
#         print(f'r = {r} is new')
#         rnd_list.append(my_list[r])
#         print(rnd_list)
#     # else:
#     #     for i in range(len(my_list)):
#     #         rnd_list.append(my_list[r])
# # print(rnd_list)