                                            # Сопоставить буквы кодам из азбуки морзе

# После каждой закодированной буквы должен стоять пробел (символ окончания кода буквы). 
# После последнего кода пробела быть не должно (в конце строки). 

# Sample Input: Сергей Балакирев
# Sample Output: ... . .-. --. . .--- -...- -... .- .-.. .- -.- .. .-. . .--

morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ё': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}

# решение 1
for i in input().lower():
    for key, value in morze.items():
        if i in key:
            print(value, end=' ')

# # решение 2
lst = []
# for i in string:
#     lst.append(morze[i])
# print(*lst)
result = [lst.append(morze[i]) for i in input().lower()]
print(*lst)

# решение 3
[print(morze.get(i), end=' ') for i in input().lower()]


                                            # Сопоставить код буквам

# Sample Input: .-- ... . -...- .-- . .-. -. ---
# Sample Output: все верно


morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ё': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}

morze.pop('ё')
result = []

for i in input().lower().split():
    for key, value in morze.items():
        if i == value:
            result.append(key)

print(''.join(result))


                            # Список уникальных чисел через словарь

# Sample Input: 8 11 -4 5 2 11 4 8
# Sample Output: 8 11 -4 5 2 4

# решение 1
lst = [int(i) for i in input().split()]
result = dict.fromkeys(lst)
for key in result.keys():
    print(key, end=' ')

# решение 2
print(*dict.fromkeys(input().split()))




                # Сформировать словарь, где ключи - дни рождения (целое число), а значения - имена (строка)

# Sample Input:
                # 3 Сергей
                # 5 Николай
                # 4 Елена
                # 7 Владимир
                # 5 Юлия
                # 4 Светлана
# Sample Output:
                # 3: Сергей
                # 5: Николай, Юлия
                # 4: Елена, Светлана
                # 7: Владимир


lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
my_dict = {}

for i in lst_in:
    key, name = i.split()  # Разделяем строку на ключ и имя
    my_dict.setdefault(key, []).append(name)  # Добавляем имя в список по ключу

# Выводим результат в нужном формате
for key, value in my_dict.items():
    print(f'{key}: {", ".join(value)}')  # Соединяем имена через запятую




                                # Собрать рюкзак в поход

# Объявите в программе словарь с наименованиями предметов и их весом (в граммах):

things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

# Сергей собирается в поход и готов взвалить на свои хрупкие плечи максимальный вес в N кг
#  (вводится с клавиатуры). Он решил класть в рюкзак предметы в порядке убывания их веса 
# (сначала самые тяжелые, затем, все более легкие) так, чтобы их суммарный вес не превысил значения N кг.
#  Все предметы даны в единственном экземпляре. Выведите список предметов (в строчку через пробел), 
# которые берет с собой Сергей в порядке убывания их веса.

# Sample Input: 10
# Sample Output: палатка брезент удочка брюки пила карандаш спички

n = int(input())*1000
things_sorted = sorted(things.items(), key=lambda item: -item[1]) # сортированный список значений словаря по убыванию

# for key, value in things_sorted:
#     if value <= n:
#         n -= value
#         print(key, end=' ')


result = [key for key, value in things_sorted if value <= n and (n:= n - value) >= 0]
print(*result)