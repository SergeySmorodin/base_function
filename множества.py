# На вход программе подается строка, содержащая латинские символы, 
# пробелы и цифры. Необходимо прочитать эту строку и выделить из нее все 
# неповторяющиеся цифры (символы от 0 до 9). 
# Выведите на экран все найденные уникальные цифры в одну строчку через пробел 
# в порядке возрастания их значений. Если цифры отсутствуют, то вывести строку "НЕТ".


# Sample Input: Python 3.9.11 - best language!
# Sample Input: Python - best language!
# Sample Output: 1 3 9

string = set(int(i) for i in input() if i.isdigit())
result = []

if len(string) == 0:
    print('НЕТ')
else:
    result = [i for i in string if i >= 0 and i <= 9]
print(*sorted(result))

# решение 2
print(*sorted(set(int(c) for c in input() if c.isdigit())) or ['НЕТ'])




                    # Требуется по списку комментариев определить уникальное число комментаторов

lst_in = ['EvgeniyK: спасибо большое!', 'LinaTroshka: лайк и подписка!', 'Sergey Karandeev: крутое видео!', 'Евгений Соснин: обожаю', 'EvgeniyK: это повтор?', 'Sergey Karandeev: нет, это новое видео']

# result = ()
# for k in lst_in:
#     key = k.split(':')[0]
#     result += key, 
# print(result)

lst = [i.split(':')[0] for i in lst_in]
print(len(set(lst)))

 
                    # Необходимо в цикле читать эти названия, пока не встретится строка "q". 

# С помощью множества определить общее уникальное число городов, которые читались в программе 
# (за исключением "q"). На экран вывести это число.

# Sample Input:
                # Уфа
                # Москва
                # Тверь
                # Екатеринбург
                # Томск
                # Уфа
                # Москва
                # q
# Sample Output: 5

s = set(i for i in iter(input, "q")) # iter() - Такая конструкция позволяет считывать в коллекцию строки до тех пор 
                                    # пока не встретит стоп-слово, в нашем случае q. input тут пишется без скобок
                                               
# s = {'Томск', 'Уфа', 'Екатеринбург', 'Тверь', 'Москва'}
print(len(s))

# решение 2
s = set()
while (city := input()) != 'q':
    s.add(city)   
print(len(s))

