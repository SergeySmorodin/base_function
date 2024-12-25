# На вход программе подается таблица целых чисел (см. пример ниже) 
# размером N x N элементов (N определяется по входным данным). 
# Необходимо прочитать эти числа и сохранить в виде двумерного (вложенного) 
# списка lst2D размером N x N элементов. Полученная таблица будет содержать нули и 
# кое-где единицы. С помощью функции с именем verify, на вход которой подается двумерный 
# список чисел (первый параметр), необходимо проверить, являются ли единицы изолированными друг 
# от друга, то есть, вокруг каждой единицы должны быть нули.

# Рекомендуется следующий алгоритм. В функции verify производить перебор 
# двумерного списка. Для каждого элемента (списка) со значением 1 вызывать 
# еще одну вспомогательную функцию is_isolate для проверки изолированности единицы. 
# То есть, функция is_isolate должна возвращать True, если единица изолирована и False в противном случае.

# Как только встречается не изолированная единица, функция verify должна возвращать False. 
# Если успешно доходим (по элементам списка) до конца, то возвращается значение True.






from colorama import init, Fore
from random import randrange
# 
# 
# def is_isolate_0(*args):
#     return sum(*args) < 2
# 
# 
# def verify_0(lst):
#     '''вариант №0 позаимствован
#      из топ представленных на форуме решений'''
#     size = len(lst)
#     return False not in [is_isolate_0(lst[i][j:j+2] + lst[i+1][j:j+2])
#                          for j in range(size - 1)
#                          for i in range(size - 1)]
# 
# 
# def is_isolate_1(y, x, check) -> bool:
#     sublist = check[y][x:x + 2] + check[y + 1][x - 1:x + 2]
#     return (sum(sublist) - 1) == 0
# 
# 
# def verify_1(lst) -> bool:
#     '''вариант решения №1 - обход по индексам'''
#     n = len(lst)
#     m = len((lst[0])) + 1
#     lst = [[0] + row for row in lst]  # добавляем нули слева (1-й столбец)
#     lst.append([0]*m)                 # и снизу, что-бы потом не выйти за матрицу
#     for i in range(n):
#         for j in range(1, m):
#             if lst[i][j]:
#                 if not is_isolate_1(i, j, lst):
#                     return False
#     return True
# 
# 
def is_isolate(columns, y, x, check) -> bool:
    launch = x - 1 if x else x                      # если индекс единички = 0 (1 столбец) - стартуем с него
    sublist = [] if y == columns else check[y+1][launch:x + 2]  # если строка не последняя, то добавляем нижнюю
    xz = check[y][x+1] if x < (len(check[y])-1) else 0
    return xz + sum(sublist)                         # True если нашли единичку в окружении


def verify(array) -> bool:
    '''вариант решения №2 - обход по строкам'''
    column_end = len(array) - 1     # некий ограничитель что-бы не вывалится за матрицу
    for i, row in enumerate(array):
        while 1 in row:                                         # пока в строке есть единицы
            one_find = row.index(1)                             # передаем в подфункцию индекс найденной
            if is_isolate(column_end, i, one_find, array):      # единички в строке и индекс строки
                return False
            row[one_find] = 0
    return True
# 
# 
# matrix = [[0]*5000 for _ in range(5000)]  # создаем тестовую матрицу из нулей
# print(Fore.LIGHTGREEN_EX + '--- ТЕСТ: проверка изолированности единицы --- '
#                            '\nДана матрица из нулей размером 5000 на 5000 элементов.')
# print(Fore.LIGHTCYAN_EX + '1. Заполнить матрицу единичками вручную'
#                           ' \n2. Сгенерировать случайное расположение единичек ')
# answer = input(Fore.LIGHTBLUE_EX + 'Выберите вариант 1 или 2: ')
# if answer == '1':
#     count = 1
#     i, j = '5000', '5000'
#     while i.isdigit() and j.isdigit():
#         int_x, int_y = int(j), int(i)
#         if 0 <= int_x < 5000 and 0 <= int_y < 5000:
#             matrix[int_y][int_x] = 1
#             print(Fore.LIGHTYELLOW_EX + f'теперь matrix[{int_y}][{int_x}] = 1')
#             count += 1
#         print(Fore.LIGHTMAGENTA_EX + f'Введите индекс строки и столбца для {count}-й единички:'
#               f'\n(для окончания введите любую букву)')
#         i = input(Fore.LIGHTBLUE_EX + 'индекс строки = ')
#         if not i.isdigit():
#             break
#         j = input('индекс столбца = ')
# elif answer == '2':
#     print(Fore.LIGHTMAGENTA_EX + 'Сколько случайно расположеных единичек сгенерировать?')
#     count = int(input(Fore.LIGHTBLUE_EX + "Число от 1 до 9'000'000: "))
#     print(Fore.LIGHTYELLOW_EX + f'Генерируем {count} единиц...')
#     for i in range(count):
#         matrix[randrange(5000)][randrange(5000)] = 1
# else:
#     print(Fore.LIGHTYELLOW_EX + 'Матрица только из нулей')
# 
# variation_func = {verify_0: 'вариант №0', verify_1: 'вариант №1', verify: 'вариант №2'}
# print(Fore.LIGHTGREEN_EX + f'{"-" * 30}\n> Старт вычислений... (wait 16 sec)')
# print(Fore.LIGHTGREEN_EX + f'> единицы изолированы? -------')
# for fn, name in variation_func.items():         # прогоняем все варианты функций
#     start_test = time.time()
#     print(Fore.LIGHTCYAN_EX + 'Результат:', fn(matrix))
#     end_test = time.time()
#     work_time = round(end_test - start_test, 2)
#     print(Fore.LIGHTBLUE_EX + f'Time = {work_time:>5} sec  # {name} \n{"-" * 30}')


# вариант с системой координат
import sys

def is_isolate(lst2D, i, j):
    # Определяем смещения для проверки соседей (вверх, вниз, влево, вправо и диагонали)
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # прямые соседи
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # диагональные соседи
    ]
    
    # Проверяем всех соседей
    for dx, dy in directions:
        ni, nj = i + dx, j + dy
        # Проверяем, находятся ли соседи в пределах границ и равны ли они 1
        if 0 <= ni < len(lst2D) and 0 <= nj < len(lst2D[0]) and lst2D[ni][nj] == 1:
            return False
    return True



lines = sys.stdin.readlines() # чтение строк из входного потока (переменную lines не менять)
lst2D = [list(map(int, i.split())) for i in lines]


def verify(lst2D):
    for i in range(len(lst2D)):
        for j in range(len(lst2D[0])):
            if lst2D[i][j] == 1:
                if not is_isolate(lst2D, i, j):
                    return False
    return True



# похожий вариант
def is_isolate(matrix, x, y):
    n = len(matrix)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < n and 0 <= y + j < n:
                if (i or j) and matrix[x + i][y + j]:
                    return False
    return True
    

def verify(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1 and not is_isolate(matrix, i, j):
                return False
    return True


# еще вариант
def is_isolate(a, x, y):
    flag = True
    n = len(a[0])

    sl_0 = [q for q in a[x-1][y-1 if y > 0 else y: y+2 if y < n else y+1]] if\
        x > 0 else []

    sl_1 = [i for i in a[x][y-1 if y > 0 else y: y+2 if y < n-1 else y+1]]

    sl_2 = [i for i in a[x+1][y-1 if y > 0 else y: y+2 if y < n else y + 1]] \
        if x < n-1 else []

    if sum(sl_0) + sum(sl_1) + sum(sl_2) != 1:
        flag = False

    return flag


def verify(t):
    for i, n in enumerate(t):
        for j, m in enumerate(n):
            if m == 1:
                if not is_isolate(t, i, j):
                    return False

    return True

