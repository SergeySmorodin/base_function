# 1
def fun():
    string = [i for i in input().split()]
    print(f"Уважаемый, {string[0]} {string[1]} Вы верно выполнили это задание!")
    

fun()


# 2
def to_do():
    weight = float(input())
    print(f"Предмет имеет вес: {weight} кг.")

to_do()

# 3
def min_max_sum(x):
    print(f'Min = {min(x)}, max = {max(x)}, sum = {sum(x)}')
    
min_max_sum(list(map(int, input().split())))


# 4
def foo(width, height):
    print(f"Периметр прямоугольника, равен {2 * (width + height)}")

width, height = map(int, input().split())
foo(width, height)



                                    # 5 Проверка коректного емейл

def check_email(email):
    # Проверяем наличие символов '@' и '.'
    if '@' not in email or '.' not in email:
        print("НЕТ")
        return
    
    # Проверяем, что все символы корректные
    valid_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_@.")
    
    for char in email:
        if char not in valid_characters:
            print("НЕТ")
            return
    
    print("ДА")

check_email(input())


 
# Функция должна возвращать булево значение True, если переданное число четное и False, в противном случае.
# Цикл должен работать пока x не равен 1. 

def is_even(x):
    return x % 2 == 0


while True:
    number = int(input())
    if number == 1:
        break
    else:
        if is_even(number) == True:
            print(number)

#  решение 2
def chet(x):
    return not x % 2

[print(i) for i in iter(input, '1') if chet(int(i))]


# решение 3
def is_even(x):
    return x % 2 == 0

lst_d = list(map(int, input().split()))
lst = [numbers for numbers in lst_d if is_even(numbers) == False] 
print(*lst)


                    # Используя генератор словарей и ранее объявленную функцию

# сформируйте на основе списка cities словарь d в формате:

# d = {<город 1>: <число символов>, ..., <город N>: <число символов>}

# Sample Input: Воронеж Лондон Тверь Омск Уфа
# Sample Output: Уфа Омск Тверь Лондон Воронеж

def search_string(string):
    return string, len(string)

# cities = ['Воронеж', 'Лондон', 'Тверь', 'Омск', 'Уфа']
cities = [city for city in input().split()]
d = {search_string(key)[0]: search_string(key)[1] for key in cities}
a = sorted(d, key=d.get)
print(*a)

# решение 2
def twix(w):
    return w, len(w)
d = {k:v for k, v in map(twix, input().split())}
a = sorted(d, key=lambda x: d[x])
print(*a)

        # Объявите в программе функцию с именем check_password, которая первым параметром принимает строку
# (пароль) и имеет второй формальный параметр chars с начальным значением в виде строки "$%!?@#".
# Функция должна проверять, есть ли в пароле хотя бы один символ из chars и что 
# длина пароля не менее 8 символов. 
# Если проверка проходит, то функция возвращает булево True, иначе False.

def check_password(string, chars="$%!?@#"):
    if len(string) > 7:
        for i in string:
            if i in chars:
                return True
    return False

# решение 2
def check_password(st, chars='$%!?@#'):
    return len(st) > 7 and any(i in chars for i in st)

# решение 3
def check_password(password):
    return bool(set(password) & set('$%!?@#')) and len(password) > 7 # через множества поиск общих символов



                                # Функция должна вернуть строку

def to_do(string, tag='h1', up=True):
    if up == True:
        tag = tag.upper()
    result = f'<{tag}>{string}</{tag}>'
    return result
  
t = input()
print(to_do(t, 'div'))
print(to_do(t, 'div', False))

# решение 2
def func(s, tag='h1', up=True):
  return (f'<{tag}>{s}</{tag}>', f'<{tag.upper()}>{s}</{tag.upper()}>')[up]
  
s = input()
print(func(s, 'div'), func(s, 'div', False), sep='\n')


                # Функция способна принимать произвольное количество чисел в качестве аргументов
                
def get_even(*args):
    result = [i for i in args if i % 2 == 0]
    return result


                # Данная функция должна возвращать название города (строку) наибольшей длины

def get_biggest_city(*args):
    return max(args, key=len)



                        #  Функция должна возвращать в виде кортежа периметр многоугольника и 
# указанные значения именованных параметров в порядке их перечисления в 
# тексте задания (если они были переданы). Если какой-либо параметр отсутствует, 
# его возвращать не нужно (пропустить).

def get_data_fig(*args, **kwargs):
    P = sum(args)
    lst = ['tp','color','closed','width']
    res = [P, *(kwargs.get(i) for i in lst if i in kwargs)]
    return tuple(res)



                # Объявите в программе функцию с именем str_min, 
                
# которая сравнивает две переданные строки (через два первых параметра) и возвращает минимальную 
# из них (то есть, выполняется лексикографическое сравнение строк). Следом объявите еще две аналогичные 
# функции:

# с именем str_min3 для поиска минимальной строки из трех переданных строк;
# с именем str_min4 для поиска минимальной строки из четырех переданных строк.
# Причем при реализации функций str_min3 и str_min4 следует использовать вызов 
# (результат работы) функции str_min.

def str_min(str1, str2):
    """Возвращает минимальную строку из двух."""
     
    return str1 if str1 < str2 else str2


def str_min3(str1, str2, str3):
    """Возвращает минимальную строку из трех, используя str_min."""
    return str_min(str_min(str1, str2), str3)

def str_min4(str1, str2, str3, str4):
    """Возвращает минимальную строку из четырех, используя str_min3."""
    return str_min3(str_min(str1, str2), str3, str4)

# Примеры использования:
print(str_min("apple", "banana"))  # apple
print(str_min3("apple", "banana", "cherry"))  # apple
print(str_min4("apple", "banana", "cherry", "date"))  # apple