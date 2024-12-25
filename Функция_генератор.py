# объявить функцию-генератор 
# которая бы возвращала max_len = N первых чисел последовательности Балакирева (включая первые три единицы).
# будем генерировать каждое последующее как сумму трех предыдущих чисел


N = 7

def balak_seq(max_len):
    a, b, c = 1, 1, 1
    count = 0
    
    while count < max_len:
        if count < 3:
            yield 1  
        else:
            next_value = a + b + c
            yield next_value
            a, b, c = b, c, next_value
        count += 1


generator = balak_seq(N)
for number in generator:
    print(number, end=' ')



# На вход программе подается натуральное число N (N > 8). 
# Необходимо его прочитать и объявить функцию-генератор, которая бы выдавала пароль длиной N 
# символов из случайных букв, цифр и некоторых других знаков. Значение N передается в функцию-генератор первым аргументом. 
# Для получения последовательности допустимых символов для генерации паролей в программе импортированы 
# две строки: ascii_lowercase, ascii_uppercase (см. листинг ниже), на основе которых формируется общий список:

# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных 
# символов chars длиной N и делать это бесконечно, то есть, вызывать ее можно бесконечное число раз.

# Сгенерируйте с помощью функции-генератора первые пять паролей и выведите их в столбик (каждый с новой строки).

# Подсказка: сгенерировать случайный индекс indx в диапазоне [a; b] для выбора символа из chars можно с помощью функции randint модуля random:

from string import ascii_lowercase, ascii_uppercase
from random import randint, seed
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
seed(1)
N = int(input())
def gen_psw(length):
    while True:
        psw = ''
        for _ in range(length):
            psw += chars[randint(0, len(chars))]
        yield psw

for _ in range(5):
    print(next(gen_psw(N)))


# задание 2
import random
from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase
random.seed(1)

def get_mail(n):
    d = []
    while True:
        a, s = '', "@mail.ru"
        for x in range(n):
            x = chars[random.randint(0, len(chars)-1)]
            a += x
        a += s
        d.append(a)    
        yield d

n = int(input())
for i in range(5):
    print(*next(get_mail(n)))
    

                                                    # Генератор простых чисел
def primes():
  """Генератор простых чисел."""
  i = 2
  while True:
    is_prime = True
    for j in range(2, int(i**0.5) + 1): # Проверяем делимость числа `i` на числа от 2 до квадратного корня из `i`
      if i % j == 0:
        is_prime = False
        break
    if is_prime:
      yield i
    i += 1

# Вывод первых 20 простых чисел
primes_generator = primes()
print(*[next(primes_generator) for _ in range(20)]) 



