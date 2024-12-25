def division(dividend, divider):
    return dividend / divider

try:
    a = int(input())
    z = int(input())
    result = division(a, z)
    print(result)
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionError:
    print('Второе число не может быть нулем')




# обработка всех исключений
def division(dividend, divider):
    return dividend / divider

try:
    a = int(input())
    z = int(input())
    result = division(a, z)
    print(result)
except:
    print("Вы ошиблись")





