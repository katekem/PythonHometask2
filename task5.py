# Написать программу, которая будет ввыводит в консоль заданный текст 
# (Python - один из самых популярных языков программирования в мире), 
# затем принимать из консоли шаблон подстроки и удалять в задданом тексте 
# все слова в которых присутствует введенный шаблон
# Пример:
# Python - один из самых популярных языков программирования в мире
# Введите подстроку: ам
# Python - один из популярных языков в мире

## Задача не решена - удаляется только для одного символа

my_text = 'Python - один из самых популярных языков программирования в мире'
my_text = my_text.split()
print(my_text)
symbol = input('Введите символ: ')
for item in my_text:
    for char in item:
        if char == symbol:
            print(f'Символ {symbol} присутствует в строке {item}')
            my_text.remove(item)
            break
    else:
        print(f'Символ {symbol} НЕ присутствует в строке {item}')
print(my_text)