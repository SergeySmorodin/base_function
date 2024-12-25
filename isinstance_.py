
                    # Функция должна складывать или два числа или две строки (но не число со строкой) и 
# возвращать полученный результат. Если сложение не может быть выполнено, то функция возвращает значение None. 
# Подсказка: не забудьте про необходимость различения булевых значений (False, True) от целочисленных 
# тк  bool наследуется от int, isinstance(a, bool) даст True на проверку числом.


# реш 1
def get_add(a, b):
    if type(a) != bool and type(b) != bool:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif type(a) is str and type(b) is str:
            return a + b

    else: return None


# реш 2
def get_add(a, b):
    if type(a) in (int, float) and type(b) in (int, float):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else: return None
    

# вызов функции
print(get_add(1, 2))
print(get_add('efefe', 'mmmn'))
print(get_add(True, 2))    # если проверять тип isinstance "a" будет 1, проверять через type(a)
print(get_add(1, 'hhghg'))
print(get_add(True, True))
print(get_add('ab', 'ra'))
print(get_add(2, 3.2))



                    # Функция принимает на входе итерируемый объект (список, строку, кортеж, словарь, множество) и вычисляет 
# сумму только целых чисел, взятых из элементов итерируемого объекта. 
# Вычисленная сумма возвращается функцией. Если целых чисел нет, то возвращается 0.

# реш 1
def get_sum(it):
    s = 0
    for i in it:
        if type(i) is int:
            s += i
    return s

# реш 2
def get_sum(it):
    return sum(filter(lambda x: type(x) is int, it))


print(get_sum([1,2,3, "a", True, [4, 5], "c", (4, 5)]))
print(get_sum({5, 6, 7, '8', 5, '4'}))
print(get_sum((10, "f", '33', True, 12)))
print(get_sum(['1', True, False, (1, 23)]))




                            # Функция принимает на входе итерируемый объект (список, строку, кортеж, словарь, множество) и вычисляет 
# сумму только целых четных чисел, взятых из элементов итерируемого объекта. 

def get_even_sum(it):
    return sum(filter(lambda x: type(x) is int and x % 2 == 0, it))




                        # Функция должна возвращать список только из числовых значений переданной ей коллекции (список или кортеж или множество).
                        # т.е исключить данные которые передаются строкой

# реш 1
def get_list_dig(lst):
    res = []
    if isinstance(lst, (list, tuple, set)):
        for i in lst:
            if type(i) in (int, float):
                res.append(i)
    if res:
        return res
    else:
        return []

# реш 2
def get_list_dig(lst):
    if isinstance(lst, (list, tuple, set)):
        return [i for i in lst if type(i) in (int, float)]
    
# реш 3
def get_list_dig(lst):
    if isinstance(lst, (list, tuple, set)):
        return list(filter(lambda x: type(x) in (int, float), lst))


print(get_list_dig([1,2,3, "a", True, [4, 5], "c", (4, 5)])) #
print(get_list_dig({5, 6, 7, '8', 5, '4'}))
print(get_list_dig((10, "f", '33', True, 12)))
print(get_list_dig(['1', True, False, (1, 23)]))

