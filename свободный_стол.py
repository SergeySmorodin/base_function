def is_table_free(n):
    """Принимает номер стола и возвращает True,
    если стол свободен, иначе False"""
    return tables.get(n) is None


def get_free_tables():
    """Возвращает список всех свободных столов."""
    return [table_num for table_num, guest in tables.items() if guest is None]


def reserve_table(n, name, is_vip=False):
    """которая принимает номер стола и имя клиента, проверяет
    свободен ли указанный столик и если за ним никто не прикреплен,
    вносятся данные клиента"""
    if is_table_free(n):
        global tables
        a = {
          n: {
            'name': name, 
            'is_vip': is_vip
            }
          }
        tables.update(a)


def delete_reservation(n):
    """очищает запись о бронировании"""
    if not is_table_free(n):
        tables[n] = None


tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False},
    6: None,
    7: None,
    8: None,
    9: None,
}

# print(tables)
reserve_table(3, 'Gena', True)
reserve_table(4, 'Artem', False)
reserve_table(5, 'Artur', True)  # Артур не должен занять место Василия
print(tables)
