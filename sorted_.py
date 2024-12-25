# Функция должна выполнить сортировку ключей словаря d по убыванию 
# (лексикографическая сортировка строк) и возвратить список из соответствующих значений ключей словаря
# ['дерево', 'лошадь', 'собака', 'кот', 'книга']

d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}


# реш 1
def get_sort(d):
    res = dict(sorted(d.items(), key=lambda item: item[0], reverse=True))
    return list(res.values())

# реш 2
def get_sort(d: dict) ->list:
    return [d.get(item) for item in sorted(d, reverse=True)] # c помощью генератора списка

# реш 3
def get_sort(d):
    res = [d[i] for i in sorted(d, reverse=True)] # d[i] получает значение из словаря
    return res


print(get_sort(d))


                # Сложить два сортированных списка, 1 по возрастанию, 2 по убыванию
# Sample Input:
# 7 6 4 2 6 7 9 10 4
# -4 5 10 4 5 65

# Sample Output:
# 67 14 9 11 10 3



a, b = map(tuple, [(int(i) for i in input().split()) for _ in range(2)])
print(*[sum(x) for x in zip(sorted(a), sorted(b, reverse=True))])


# реш 2
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)
print(*map(lambda x,y: x+y, a, b))



                              # Задача сформировать словарь, написать функцию которая принимает словарь и выдает 3 минимальных значения
# Sample Input:
# смартфон:120000
# яблоко:2
# сумка:560
# брюки:2500
# линейка:10
# бумага:500

# Sample Output:
# яблоко линейка бумага

# Также необходимо написать функцию, которая бы принимала на входе 
# словарь указанного формата и возвращала список из наименований трех наиболее дешевых товаров.

lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']

my_dict = {int(value): key.strip() for key, value in (line.split(':') for line in lst_in)} # формируем словарь и меняем ключи и значения местами


def get_cheapest_items(price_dict):
    sorted_prices = sorted(price_dict) # Сортируем цены по возрастанию
    cheapest_items = [price_dict[price] for price in sorted_prices[:3]] # Берем первые 3 цены и получаем соответствующие наименования
    return cheapest_items


cheapest_items = get_cheapest_items(my_dict)
print(cheapest_items)


# реш 2
d = {k: v for k, v in map(lambda x: x.split(':'), lst_in)}  # получения ключ значения с помошью мап!!!!!!

srtd = sorted(d.items(), key=lambda x: int(x[1]))[:3]

for item in srtd:
    print(item[0], end=' ')


                            # сортировать использую заданный список
# Sample Input:
# до фа соль до ре фа ля си

# Sample Output:
# до до ре фа фа соль ля си


lst = ['до', 'фа', 'соль', 'до', 'ре', 'фа', 'ля', 'си']  # входящий список, который нужно отсортировать

# реш 1
d = {'до': 1, 'ре': 2, 'ми': 3, 'фа': 4, 'соль': 5, 'ля': 6, 'си': 7} # задаем словарь для ключа сортировки
print(*sorted(lst, key=d.get))

# реш 2
notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'] # задаем список для ключа сортировки
print(sorted(lst, key=lambda x: notes.index(x))) # передаем индекс списка как ключ


                # Данные этого списка необходимо разбить по разделителю ";" и представить в виде двумерного (вложенного) кортежа в формате:
# ( ('Номер', 'Имя', 'Оценка', 'Зачет'), (1, 'Иванов', 3, 'Да'), (2, 'Петров', 2, 'Нет'), ... )


lst_in = ['Номер;Имя;Оценка;Зачет', '1;Портос;5;Да', '2;Арамис;3;Да', '3;Атос;4;Да', "4;д'Артаньян;2;Нет", '5;Балакирев;1;Нет']

