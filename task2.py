# Задайте список из n чисел последовательности (1 + 1/n)^n. 
# Вывестив консоль сам список и сумму его элементов.
n = int(input('Введите n больше нуля: '))
my_list = []
if n <= 0:
    print('Введено число меньше или равное нулю')
else:
    sum = 0
    for i in range(n):
        my_list.append(round(((1+1/n)**n),2))
        n = (1+1/n)**n
        sum += n
    print(my_list)
    print(f'Сумма элементов = {round(sum, 2)}')
   