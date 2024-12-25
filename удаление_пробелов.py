# Удаление лишних пробелов из списка
lst_in = ['django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya', 'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']

cleaned_lst = []    # Создаем новый список для хранения очищенных строк

for string in lst_in:
    # Убираем лишние пробелы и заменяем их на '-'
    cleaned_string = '-'.join(string.split())
    cleaned_lst.append(cleaned_string)

# Выводим результат
for i in cleaned_lst:
    print(i)


    