                                # Добавить элемент в картеж

# Необходимо сформировать кортеж из названий городов. 
# Названия в кортеже должны идти в том же порядке, что и в исходной строке. 
# Выполните проверку: если в полученном кортеже нет города "Москва", то следует его добавить 
# в конец кортежа. Выведите на экран названия городов из кортежа (по порядку) в одну строчку через пробел.


# test #1
# input: Уфа Казань Самара
# output: Уфа Казань Самара Москва
t = tuple(input().split())
if 'Москва' not in t:
        t += 'Москва',
print(*t)



                                  # Удалить елемент из картежа

# Необходимо сформировать кортеж из названий городов. 
# Затем, выполните проверку: если в полученном кортеже присутствует город "Ульяновск", 
# то этот элемент следует удалить (создав новый кортеж). Выведите на экран названия городов 
# из итогового кортежа (по порядку) в одну строчку через пробел.

# Sample Input: Воронеж Самара Тольятти Ульяновск Пермь
# Sample Output: Воронеж Самара Тольятти Пермь
cities = tuple(input().split())
c = ()
for i in cities: 
    if i != 'Ульяновск':
        c = c + (i,)
print(*c)



                            # Необходимо сформировать кортеж из имен. 

# Затем, отобразите на экране все имена малыми буквами из этого кортежа (по порядку), 
# которые содержат фрагмент "ва" (без учета регистра). 
# Имена выводятся в одну строчку через пробел в нижнем регистре (малыми буквами)

# Sample Input: Петя Варвара Венера Василиса Василий Федор
# Sample Output: варвара василиса василий

names = tuple(i for i in input().lower().split())
names_ = ()
for name in names:
    if name.count('ва'):
        names_ += name, 
print(*names_)

# решение 2
print(*tuple(i for i in input().lower().split() if "ва" in i))




                # Создать еще один кортеж с уникальными (не повторяющимися) значениями из первого кортежа. 

# Уникальные числа должны следовать в том же порядке, что и в исходном кортеже. 

# Sample Input: 8 11 -5 -2 8 11 -5
# Sample Output: 8 11 -5 -2

# numbers = tuple(int(i) for i in input().split())
numbers = (8, 11, -5, -2, 8, 11, -5)
result = ()

for number in numbers:
    if number not in result:
        result += number,
print(result)

# решение 2
print(*(dict.fromkeys(tuple(input().split())))) # ключи словаря не могут повторяться



                # Найти и вывести в одну строчку через пробел (по порядку) все индексы неуникальных 
                                    # (повторяющихся) значений.

# Sample Input: 5 4 -3 2 4 5 10 11
# Sample Output: 0 1 4 5

# numbers = tuple(int(i) for i in input().split())
numbers = (5, 4, -3, 2, 4, 5, 10, 11)

result = ()
for i, number in enumerate(numbers):
    if numbers.count(number) > 1:
        print(i, end = ' ')

# решение 2
t = tuple(input().split())
repeat_values = tuple(i for i, v in enumerate(t) if t.count(v) > 1)
print(*repeat_values)


                # Объявите в программе следующий двумерный кортеж, размером 5 x 5 элементов:

t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))

# На вход программе подается натуральное число N (N < 5). 
# Необходимо на основе кортежа t сформировать новый аналогичный кортеж t2 размером N x N 
# элементов путем отбрасывания последних строк и столбцов. 

# Sample Input: 3
# Sample Output:
                # 1 0 0
                # 0 1 0
                # 0 0 1

# решение 1
x = int(input())
t2 = ()
for i in t:
    i = i[:x]
    t2 += i,

for i in t2[:x]:
    print(*i)

# # решение 2
n = int(input())
t1 = tuple([[t[i][j] for i in range(n)] for j in range(n)])
[print(*i) for i in t1]

# решение 3
n = int(input())
t2 = tuple([i[:n] for i in t[:n]])
[print(*i) for i in t2]



                # Необходимо преобразовать список lst_in так, чтобы получился кортеж menu следующего вида:

# Sample Input:
                # Главная home
                # Python learn-python
                # Java learn-java
                # PHP learn-php

# Sample Output:
# (('Главная', 'home'), ('Python', 'learn-python'), ('Java', 'learn-java'), ('PHP', 'learn-php'))

lst_in = ['Главная home', 'Python learn-python', 'Java learn-java', 'PHP learn-php']

menu = tuple(tuple(i.split()) for i in lst_in)
print(menu)

# решение 2
print((*map(tuple, map(str.split, open(0))),))

