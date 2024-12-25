                                                            # варианты генератора словарей!!!!!!!!!!!
# 1
d = dict(s.split("=") for s in lst_in)
# 2
d = dict(map(lambda x: x.split('='), lst_in))
# 3
d = {key: int(value) for item in lst_in for key, value in [item.split('=')]}
# 4
d: dict = {value.split('=')[0]: int(value.split('=')[1]) for value in lst_in}
# 5
d = {i.split('=')[0]: i.split('=')[1] for i in lst_in}
# 6
d = dict(zip([i.split('=')[0] for i in lst_in], [int(i.split('=')[1]) for i in lst_in]))
# 7
d = {k: int(v) for k,v in [x.split('=') for x in lst_in]}
# 8
d = {}
for item in lst_in:
    key, value = item.split("=")
    d[key] = int(value)                                

    
                                                            # Сформировать словарь из строки

# Sample Input: one=1 two=2 three=3
# Sample Output: ('one', 1) ('three', 3) ('two', 2)

# решение 1
# lst = input().split()
lst = ['one=1', 'two=2', 'three=3']
d = {}
for item in lst:
    key, value = item.split('=')
    d[key] = int(value)
print(*sorted(d.items()))

# решение 2 
lst = [[int(j) if j.isdigit() else j for j in i.split('=')] for i in input().split()]
d = dict(lst)
print(*sorted(d.items()))

# решение 3
d = dict([[item.split("=")[0], int(item.split("=")[1])] for item in input().split()])
print(*sorted(d.items()))

# решение 4 без преобразования к int
lst = ['one=1', 'two=2', 'three=3']
d = dict([item.split("=") for item in lst])
print(*sorted(d.items()))


                                    # Найти ключи в словаре

# проверить, существуют ли в словаре ключи со значениями: 'house', 'True' и '5'

# решение 1
lst = ['вологда=город', 'house=дом', 'True=1', '5=отлично', '9=божественно']
d = dict([key.split('=') for key in lst])
if 'house' in d and 'True' in d and '5' in d:
    print("ДА")
else:
    print("НЕТ")

# решение 2
d = dict(i.split('=') for i in input().split())
check = ['house', 'True', '5' ]
print(['НЕТ','ДА'][all([i in d for i in check])])


                                        # Удалить ключи из словаря

# удалить 'False', '3', если они есть в словаре
# input: лена=имя дон=река москва=город True=истина three=3 ложь=False
# input: лена=имя дон=река москва=город False=ложь 3=удовлетворительно True=истина
# output: ('True', 'истина') ('three', '3') ('дон', 'река') ('лена', 'имя') ('ложь', 'False') ('москва', 'город')

# решение 1
d = {k: v for item in input().split() for k, v in [item.split('=')] if k not in ('False', '3')}
print(*sorted(d.items()))

# решение 2
lst = [i for i in input().split()]
d = dict([key.split('=') for key in lst])
if 'False' in d:
    del d['False']
if '3' in d:
    del d['3']
print(*sorted(d.items()))



                                                         # Сформировать словарь из списка номеров

# На вход программе подаются номера телефонов, с разными кодами стран: +7, +6, +2, +4 и т.д. 
# Необходимо сформировать словарь d. Ключами словаря должны быть коды (строки: +7, +6, +2 и т. п.), 
# а значениями список номеров в виде строк (следующих в том же порядке, что и в исходной строке) 
# с соответствующими кодами. 

# Sample Input: +71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
# Sample Output: ('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])

# решение 1
iter_object = [i for i in input().split()]
d = {}
for i in iter_object:
    d.setdefault(i[:2], []).append(i)   # создаётся новая пара в словарь с КЛЮЧОМ 'key'и ЗНАЧЕНИЕМ - [] пустой список. 
                                        # если такой ключ в словаре уже есть, то метод setdefaultне меняет его значение
                                        # метод возвращает значение из словаря. Если такого ключа раньше не было, то он вернёт 
                                        # только что созданный пустой список, если же такой ключ был, то он вернёт тот список, который был.
                                        # И в этот список можно добавлять любые значения, чем, собственно, append('value')и занимается.
print(*sorted(d.items()))


# решение 2
d = input().split()
d = {i[:2]: [x for x in d if x[:2] == i[:2]] for i in d}
print(*sorted(d.items()))


                                                            # Сформировать словарь из списка ключ значение

# Sample Input:
# +71234567890 Сергей
# +71234567810 Сергей
# +51234567890 Михаил
# +72134567890 Николай
# Sample Output:
# ('Михаил', ['+51234567890']) ('Николай', ['+72134567890']) ('Сергей', ['+71234567890', '+71234567810'])

# На вход программе поступают номера телефонов с привязкой к именам в виде строк следующего формата:
# номер_1 имя_1
# В программе уже реализовано считывание всех строк и сохранение их в виде списка:
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['+71234567890 Сергей', '+71234567810 Сергей', '+51234567890 Михаил', '+72134567890 Николай']

# На основе списка lst_in необходимо создать словарь d, где ключами будут имена, 
# а значениями - список номеров телефонов для этого имени (ключа). 
# Обратите внимание, что одному имени может принадлежать несколько разных номеров. 

# решение 1
d = {}
for item in lst_in:
    value, key = item.split()
    d.setdefault(key, []).append(value) 
print(*sorted(d.items()))

# решение 2
d = {}
for item in lst_in:
    value, key = item.split()
    d[key] = d.get(key, []) + [value]
print(*sorted(d.items()))


                            # Преобразовать список в словарь, где ключи целые значения
# Sample Input:
# смартфон:120000
# яблоко:2
# сумка:560
# брюки:2500
# линейка:10
# бумага:500

# Sample Output:
# яблоко линейка бумага

lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']

# вариант 1
d = dict([key.split(':') for key in lst_in])
reversed_dict = {int(value): key for key, value in d.items()}
# print(reversed_dict)

# вариант 2
my_dict = {}
for line in lst_in:
    key, value = line.split(':')
    my_dict[int(value)] = key.strip() # присваиваем  ключ и значение
# print(my_dict)


# вариант 3!!!
my_dict = {int(value): key.strip() for key, value in (line.split(':') for line in lst_in)}
print(my_dict)

# вариант 4
d = {k: v for k, v in map(lambda x: x.split(':'), lst_in)}  # получения ключ значения с помошью мап!!!!!!


