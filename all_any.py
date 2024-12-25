# определить, являются ли все эти числа четными. 
# Вывести True, если это так и False в противном случае.

# Sample Input:
# 2 4 6 8 22 56

# Sample Output:
# True

n = [2, 5, 6, 8, 22, 56]

# реш 1
def is_even(lst):
    return all(i % 2 == 0 for i in lst) 

print(is_even(n))

# реш 2
print(all(map(lambda p: p % 2 == 0, n)))




                            # определить, есть ли среди них хотя бы одно отрицательное

n = [8.2, -11.0, 20, 3.4, -1.2]                           
print(any(map(lambda x: x < 0, n)))


                    # Функция должна возвращать True, если все элементы коллекции lst - строки и 
                    # False в противном случае.
a = ["1", "москав", "Париж"]


def is_string(lst):                        
    if not lst:
        return False
    return all(isinstance(i, str) for i in lst)

print(is_string(a))


                        # На вход программе подается текущее игровое поле для игры "Крестики-нолики" в виде следующей таблицы (списка строк):
# Здесь # - свободная клетка. В программе уже реализовано чтение этих строк и сохранение в список lst_in:
# Необходимо преобразовать этот список строк в двумерный список с именем pole вида (пример):
# [ ['#', 'x', 'o'], ['x', '#', 'x'], ['o', 'o', '#'] ]
# Данная функция должна возвращать True, если есть хотя бы одна свободная клетка и False в противном случае.

# input: 
# # x o
# x # x
# o o #
# output: True

lst_in = ['# x o', 'x x x', 'o o x']

# pole = [[i for i in x.split()] for x in lst_in]  # [['#', 'x', 'o'], ['x', '#', 'x'], ['o', 'o', '#']]
pole = [i.split() for i in lst_in] # [['#', 'x', 'o'], ['x', 'x', 'x'], ['o', 'o', 'x']]

def is_free(lst):
    for elem in lst:
        return any(map(lambda x: x == '#', elem))
    
# реш 2
def is_free(lst):
    return any('#' in i for i in lst)
