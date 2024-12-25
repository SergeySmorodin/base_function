                                # Проверка формата телефона

# number = '+7(123)456-78-99'
# number = '+7 123-456-78-99'
# number = '-7(123)456-78-99'
# number = '+7(aaa)345-78-99'
# number = '+7(123)-6f-66-77'
# number = '+7(123)656-66-77'
# # number = '+8(123)656-66-77'
# # number = '+7(123)656 66-77'
# # number = '+7(123)656-66 77'
# # number = '+7(123)656-aa-77'
number = '+7(1!3)656-66-77'

expect_string = '+7(xxx)xxx-xx-xx'
lst = []
fl = 'ДА'

if len(number) != len(expect_string) or number[0] != '+' or number[1] != '7' or number[2] != '(' or number[6] != ')' or number.count('-') < 2:
    fl = 'НЕТ'
else:
    for i in range(len(number)):
        if expect_string[i] == 'x':
            if number[i].isdigit():
                lst.append(number[i])
            else:
                lst.append(f'по {i} индексу не число')
        
        else:
            lst.append(number[i])

if ''.join(lst) == number:
    fl = 'ДА'
else:
    fl = 'НЕТ'


                            #  решение с помощью регулярных выражений
import re

def validate_phone_number(number: str) -> str:
    # Ожидаемый формат номера телефона
    expect_pattern = r'^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$'
    
    # Проверка формата номера с помощью регулярного выражения
    if re.match(expect_pattern, number):
        return 'ДА'
    else:
        return 'НЕТ'

