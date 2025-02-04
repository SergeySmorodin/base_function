                # Необходимо прочитать эту строку и с помощью генератора словарей сформировать словарь d, 
                        # в котором ключами будут выступать числа, а значениями - слова.

# Sample Input:
        # 1 ужасно неудовлетворительно удовлетворительно прилично отлично
# Sample Output:
        # прилично

a = input().split()
my_dict = {i : d for i, d in enumerate(a[1:], int(a[0]))} #генератор словаря
print(my_dict[4])





              #  Cформировать множество из уникальных слов без учета регистра и длина которых не менее трех символов
                                # как я вышел как я ушел
lst = {i for i in input().lower().split() if len(i) > 2}
print(len(lst))




                        #  C помощью генераторов множеств и словарей сформировать словарь в формате:

# {слово_1: количество_1, слово_2: количество_2, ..., слово_N: количество_N}

# То есть, ключами выступают уникальные слова (без учета регистра), 
# а значениями - число их встречаемости в тексте. 
# На экран вывести значение словаря для слова (союза) 'и'. Если такого ключа нет, то вывести 0.

# Sample Input:
        # И что сказать и что сказать и нечего и точка
# Sample Output:
        # 4

lst = [i for i in input().lower().split()]
s = {key: lst.count(key) for key in set(lst)}

print(s.setdefault('и', 0))

# решение 2 без множеств
print(input().lower().split().count('и'))


        # Создать словарь из входящих данных, где ключи автор, значение книги

# Пушкин: Сказака о рыбаке и рыбке
# Есенин: Письмо к женщине
# Тургенев: Муму
# Пушкин: Евгений Онегин
# Есенин: Русь

lst_in = ['Пушкин: Сказака о рыбаке и рыбке', 'Есенин: Письмо к женщине', 'Тургенев: Муму', 'Пушкин: Евгений Онегин', 'Есенин: Русь']

d = {author.split(':')[0]: set() for author in lst_in}
for item in lst_in:
    author = item.split(':')[0]
    book = item.split(':')[1].lstrip()
    d[author].add(book)
print(d)

# решение 2
d = {i.split(':')[0] : {j.split(': ')[1] for j in lst_in if i.split()[0]==j.split()[0]} for i in lst_in}

# решение 3
d = {}
for line in lst_in:
    name, book = line.split(': ')
    d.setdefault(name, set()).add(book)
    
# решение 4
lst = [i.split(":") for i in lst_in]
d = {}
{d.setdefault(i[0], set()).add(i[1].strip()) for i in lst}

