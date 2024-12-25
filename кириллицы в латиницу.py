# Объявите в программе функцию, которая первым параметром принимает строку (с кириллицей и латиницей) 
# и преобразовывает в ней кириллические символы в латиницу, используя следующий словарь для 
# замены русских букв на соответствующее латинское написание:

# Функция должна возвращать результат преобразования переданной строки в латиницу. 
# Замены делать без учета регистра (исходную строку вначале следует перевести в 
# нижний регистр - малые буквы).

# Второй формальный параметр функции с именем sep и начальным значением в виде строки "-". 
# Он определяет символ для замены пробелов в строке.

# На вход программе подается строка, которую необходимо прочитать (после объявления функции). 
# Затем, дважды вызовите функцию (с выводом результата ее работы на экран):

# первый раз только с прочитанной строкой;
# второй раз с прочитанной строкой и именованным аргументом sep со значением '+'.

# Sample Input:
        # Лучший курс по Python!

# Sample Output:
        # luchshiy-kurs-po-python!
        # luchshiy+kurs+po+python!

                      
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def get_lat(string, sep='-'):
    string = string.lower().replace(' ', sep) 
    n_s =  ''
    for s in string: 
        n_s += t.get(s, s)
    return n_s

text = input()
print(get_lat(text))
print(get_lat(text, sep='+'))


# решение 2
def func (s, sep='-'):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
    'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
    'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', ' ': sep}
    # в словарь добавляем пробел с ключем sep
    return "".join([t.get(x,x) for x in s.lower()])

s = input()
print(func(s))
print(func(s, sep='+'))


# решение 3
def transliterate(text, sep='-'):
    return ''.join(t.get(i, i) for i in text.lower()).replace(' ', sep)

s = input()
print(transliterate(s))
print(transliterate(s, sep='+'))

# решение 4
# Идем по словарю и меняем символы в строке, отдельно меняем пробел на sep:
def to_latin(s, sep='-'):
    s = s.replace(' ', sep)
    for key, value in t.items():
        s = s.replace(key, value)
    return s
    
s = input().lower()
print(to_latin(s))
print(to_latin(s, '+'))

# решение 5
# с помощью встроенных методов для строк: translate, maketrans.
def trans(s: str, sep='-'):
    return s.replace(' ', sep).translate(s.maketrans(t))

s1 = input().lower()
print(trans(s1))
print(trans(s1, sep='+'))



                    # Перевод в латиницу с помошью ДЕКОРАТОРОВ

# Небуквенные символы " : ;.,_" превращать в символ '-' (дефиса).
# Определите декоратор для этой функции, который несколько подряд идущих дефисов, 
# превращает в один дефис.

# Sample Input:
# Python - это круто!

# Sample Output:
# python-eto-kruto!

import re

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        while "--" in res:
            res = res.replace("--", "-")
        return res
    return wrapper

@decorator
def transliterate(text):
    string = ''.join(t.get(i, i) for i in text.lower())
    return re.sub(r'[ :;.,_]', '-', string.strip())


s = str(input())
c = transliterate(s)
print(c)  


# решение 2
def remove(func):
    def wrapper(stroka):
        ls = func(stroka).replace('-', ' ').split()
        return '-'.join(ls)
    return wrapper

@remove
def cyrillic_to_latin(strings):
    lst = [t.get(i, i) if i not in [":", ";", '.', ',', ' '] else '-' for i in strings.lower()]
    return ''.join(lst)

s = input()
print(cyrillic_to_latin(s))


# решение 3 с добавлением ключей в словарь
t.update(dict.fromkeys(" :;.,_", '-'))

def remove_extra_hyphens(func):
    def wrapper(s):
        s = func(s)
        i = s.find('--')
        while i != -1:
            s = s.replace('--', '-')
            i = s.find('--', i)
        return s
    return wrapper
    
@remove_extra_hyphens
def rus_to_lat(s):
    return s.lower().translate(str.maketrans(t))

print(rus_to_lat(input()))

# решение 4
def decorator(func):
    def inner(*args, **kwargs): 
        result = func(*args, **kwargs)
        while '--' in result:
            result = result.replace('--', '-')
        return result
    return inner

@decorator
def translate(value):
    return ''.join(['-' if i in " :;.,_" else t.get(i, i) for i in value.lower()])    
      
s = input()
print(translate(s))


                                                            # с помощью мап

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
s = input()
st = ''.join(list(map(lambda x: t[x] if x in t else '-', s.lower())))
print(st)

