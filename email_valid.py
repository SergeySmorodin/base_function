# На вход программе подается строка с email-адресами, записанных через пробел. 
# Нужно прочитать эту строку и среди email-адресов оставить только корректно записанные адреса. 
# Полагается, что к таким относятся те, что используют только латинские буквы, цифры и символ подчеркивания. 
# Также в адресе должен быть символ "@", а после него символ точки "." (между ними, конечно же, могут быть и другие символы).
# Результат отобразить в виде строки email-адресов, записанных через пробел в порядке их следования в исходной строке.

# Sample Input:
# abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com

# Sample Output:
# abc@it.ru biba123@list.ru sc_lib@list.ru


# решение 1 регулярки
import re
# Считываем входные данные
emails = input("Введите email-адреса через пробел: ")

# Регулярное выражение для проверки корректности email
email_pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_.]+\.[a-zA-Z]{2,}$'

# Разделяем строку на адреса и фильтруем их
valid_emails = [email for email in emails.split() if re.match(email_pattern, email)]

# Выводим результат в виде строки через пробел
print(" ".join(valid_emails))




# решение 2
def is_valid_email(email):
    # Проверяем, содержит ли email символ '@' и хотя бы одну '.'
    if '@' not in email or '.' not in email.split('@')[1]:
        return False
    
    # Разделяем email на части
    local_part, domain_part = email.split('@')
    
    # Проверяем, что локальная часть состоит только из допустимых символов
    if not all(c.isalnum() or c == '_' for c in local_part):
        return False
    
    # Проверяем, что доменная часть состоит только из допустимых символов
    # Доменная часть может содержать буквы, цифры и точки
    if not all(c.isalnum() or c == '.' for c in domain_part):
        return False
    
    return True

emails = input().split()
valid_emails = filter(is_valid_email, emails)

# Объединение корректных адресов в строку
result = ' '.join(valid_emails)
print(result)