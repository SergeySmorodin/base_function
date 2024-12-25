# Создать словарь и записать в файл.txt

catalog = {}
for i in range(3):
    k = input('Введите наименование:')
    v = int(input('Введите количество товара:'))
    if k in catalog:
        catalog[k] += v
    else:
        catalog[k] = v

with open('test.txt', 'w', encoding='utf-8') as f:
    for k, v in catalog.items():
        f.write(f"{k}: {v}" + '\n')



# Создать словарь и записать в файл.csv
import csv

catalog = {}
with open('test.csv', 'r+') as f:
    rows = csv.reader(f)
    for tov, kol in rows:
        catalog[tov] = int(kol)
    for _ in range(3):
        tov = input('Наименование товара ')
        kol = int(input('Количество товара '))
        if tov in catalog:
            catalog[tov] += kol
        else:
            catalog[tov] = kol
with open('test.csv', 'w') as f:
    writer = csv.writer(f)
    for i in catalog.items():
        writer.writerow(i)