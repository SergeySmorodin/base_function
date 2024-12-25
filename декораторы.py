                        # универсальный декоратор-тестировщик
import time

def test_time(fn):
    def wrapper(*args, **kwargs):
        st = time.time() # вычисляем время запуска функции
        res = fn(*args, **kwargs)
        dt = time.time() - st # вычисляем разницу времени окончания работы функции и запуском
        print(f"Время работы: {dt} сек")
        return res
 
    return wrapper


# медленный алкоритм Евклида для теста
@test_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


# быстрый алкоритм Евклида для теста
@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

# Вывод результата

# get_nod = test_time(get_nod)             равноценно @test_time
# get_fast_nod = test_time(get_fast_nod)   равноценно @test_time
res = get_nod(2, 1000000)
res2 = get_fast_nod(2, 1000000)
print(res, res2)




                # Определите декоратор func_show для этой функции, который отображает 
# результат на экране в виде строки (без кавычек):
# "Площадь прямоугольника: <значение>"

# решение 1 
def func_show(fn): # функция декоратор
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        print(f'Площадь прямоугольника: {res}')
        return res
    return wrapper
        
def get_sq(width, height):
    P = width * height
    return P


# решение 2
def get_sq(width, height):
    return width * height

def func_show(func): # функция декоратор
    def wrapper(*args, **kwards):
        print(f'Площадь прямоугольника: {func(*args, **kwards)}')
    return wrapper




            # На вход программы поступает строка с названиями пунктов меню, 
# записанные в одну строчку через пробел. В программе реализовано чтение этой строки командой:

# menu = input()
# Необходимо задать функцию с именем get_menu с сигнатурой:

# def get_menu(s): ...
# которая преобразует переданную ей строку s в список из слов и возвращает этот список.

# Определите декоратор для этой функции с именем show_menu, который отображает список на экран в формате:
# 1. Пункт_1

# Sample Input:
                # Главная Добавить Удалить Выйти

# Sample Output:
                        # 1. Главная
                        # 2. Добавить
                        # 3. Удалить
                        # 4. Выйти

# решение 1
menu = input() # чтение пунктов меню (переменную menu не менять)

def show_menu(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        res_2 = [f'{i}. {j}' for i, j in res]
        for i in res_2:
            print(i)
    return wrapper


@show_menu
def get_menu(s):
    s = s.split()
    d = []
    for i, item in enumerate(s, 1):
        d.append([i, item])
    return d

# решение 2
def show_menu(func):
    def wrapper(*args, **kwargs):
        for i, item in enumerate(func(*args, **kwargs), start=1):
            print(f'{i}. {item}')
    return wrapper        
            
@show_menu
def get_menu(s):
    return s.split()


# получить сортированный список с помощью функции декоратора
def get_list(funk):
    def wrapper(*args, **kwargs):
        res = funk(*args, **kwargs)
        return sorted(res)
    return wrapper

@get_list
def get_string(text):
    s = [int(i) for i in text.split()]
    return s

s = input()
lst = get_string(s)
print(*lst)



            # Декоратор для этой функции, который из двух списков формирует словарь, 
# в котором ключами являются слова из первого списка, а значениями

# Sample Input:
                # house river tree car
                # дом река дерево машина
# Sample Output:
# ('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')

def dictionary_decorator(func):
    def wrapper(*args, **kwargs):
        list1, list2 = func(*args, **kwargs)
        result_dict = dict(zip(list1, list2))
        return result_dict
    return wrapper

@dictionary_decorator
def get_lists(str1, str2):
    list1, list2 = str1.split(), str2.split()
    return list1, list2

a = input()
b = input()

d = get_lists(a, b)
print(*sorted(d.items()))



