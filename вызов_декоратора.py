from functools import wraps

def df_decorator(start=5):
    def decorator(fn):
        @wraps(fn) # сохранение имени функции при вызове __name__ будет get_digit (нужен импорт wraps)
                        # равноценно wrapper.__name__ = fn.__name__
        def wrapper(*args, **kwargs):
            res = fn(*args, **kwargs) + start           
            return res
        # wrapper.__name__ = fn.__name__
        # wrapper.__doc__ = fn.__doc__
        return wrapper
    return decorator


@df_decorator(start=10) # задаем параметр для декоратора 
def get_digit(string):
    res = sum([int(i) for i in string.split()])
    return res


n = input()
print(get_digit(n))


                    # Примените декоратор со значением tag="div" к функции и вызовите 
# декорированную функцию для строки s, прочитанной из входного потока:

# Sample Input:
# Декораторы - это классно!

# Sample Output:
# <div>декораторы - это классно!</div

def df_decorator(tag="h1"):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            res = f'<{tag}>{fn(*args, **kwargs)}</{tag}>'
            return res
        wrapper.__name__ = fn.__name__
        return wrapper
    
    return decorator

@df_decorator("div")
def string_lower(string):
    string = string.lower()
    return string


s = input()
print(string_lower(s))


                # Определите декоратор с параметром chars и начальным значением " !?", 
# который данные символы преобразует в символ "-" и, кроме того, все подряд 
# идущие дефисы (например, "--" или "---") приводит к одному дефису. 
# Полученный результат должен возвращаться в виде строки.

# Примените декоратор с аргументом chars="?!:;,. " к функции и вызовите 
# декорированную функцию для строки s:

# Sample Input:
# Декораторы - это круто!

# Sample Output:
# dekoratory-eto-kruto-

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

def df_decorator(chars="!?"):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            # Получаем результат вызова функции
            res = fn(*args, **kwargs)
            # Приводим к строке
            res = ''.join(res)
            # Заменяем указанные символы на дефис
            for char in chars:
                res = res.replace(char, '-')
            # Убираем несколько подряд идущих дефисов
            while '--' in res:
                res = res.replace('--', '-')
            return res
        wrapper.__name__ = fn.__name__  # Сохраняем имя функции
        return wrapper   
    return decorator

@df_decorator(chars="?!:;,. ")
def translate(value):
    # Преобразуем строку в нижний регистр и заменяем буквы
    res = [t.get(i, i) for i in value.lower()]
    return res

# Пример использования
s = input("Введите строку: ")
print(translate(s))


                        # '''Функция для формирования списка целых значений'''
# Внутри декоратора декорируйте переданную функцию с помощью команды @wraps 
# (не забудьте сделать импорт: from functools import wraps).                        

from functools import wraps

def decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        sum_numbers = sum(res)
        return sum_numbers
    # wrapper.__name__ = fn.__name__
    # wrapper.__doc__ = fn.__doc__
    return wrapper

@decorator
def get_list(numbers):
    '''Функция для формирования списка целых значений'''
    res = [int(i) for i in numbers.split()]
    return res


