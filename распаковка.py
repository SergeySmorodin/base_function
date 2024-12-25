                # Объединить 2 словаря

lst_in = ['название_1=url_1', 'название_2=url_2']
menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}

# d = {}
# for i in lst_in:
#     k, v = i.split('=')
#     d[k] = v

d = {k: v for k, v in [i.split('=') for i in lst_in]}
menu = {**menu, **d}
        
print(menu)
