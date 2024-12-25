import time


def get_nod(a, b):
    """Вычисляется наибольший общий делитель (НОД) для натуральных чисел a и b
        по алгоритму Евклида.
        Возвращает вычисленный НОД.
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
 
    return a


# быстрое решение
def get_fast_evclid(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


# Классический вариант 
def get_nod(a, b):
    # Не нужно менять местами a и b, если b < a,
    # т.к. после первой итерации само поменяется
    while b:
        a, b = b, a % b
    return a


# классика с рекурсией
def get_nod(a, b):
    return get_nod(b, a % b) if b else a


#  рекурсия в одну строку
get_nod = lambda a, b: get_nod(b, a % b) if b else a

# использование функции gcd из модуля  math, самый короткий вариант
get_nod = __import__("math").gcd



# Тесты
def test_nod(func):
    # -- тест №1 -------------------------------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("#test1 - ok")
    else:
        print("#test1 - fail")
 
    # -- тест №2 -------------------------------
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("#test2 - ok")
    else:
        print("#test2 - fail")
 
    # -- тест №3 -------------------------------
    a = 2
    b = 10000000
 
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print("#test3 - ok")
    else:
        print("#test3 - fail")

# тестирование функции
test_nod(get_nod)


