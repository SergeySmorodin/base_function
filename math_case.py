fio = ('Сидоров', 'Петр', 'Иванович')

match fio:
    case f1, f2, f3:
        res = ", ".join([f2, f3, f1])
    case _:
        res = "Некорректный формат данных"

print(res)


            # С помощью оператора match/case в функцию parse_json добавьте в самое начало шаблон для выделения значения 
# ключа access с проверкой на тип bool и для выделения даты (первое значение списка) из поля data с проверкой, 
# что data является списком. Возвратите выделенные два значения в виде кортежа в формате (access, date).

def parse_json(data):
    match data:
        case {'access': bool() as access, 'data': list([date, *_])}:
            return (access, date)
        
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None

json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}



                            # С помощью оператора match/case в функцию parse_json добавьте в самое начало шаблон для выделения 
# значений ключей login и email с проверкой, что они являются строками и при условии, что поле access 
# принимает значение True. Возвратите выделенные два значения в виде кортежа в формате (login, email).


def parse_json(data):
    match data:
        case {'access': True, 'data': [_, {'login': str(login), 'email': str(email)}, *_]}:
            return login, email
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None

json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}



                        # Проверка на соответствие константе

# пропишем констатны в отдельном классе или в другой файле и импортируем файл
class Consts:
    CMD_3 = 3
    CMD_5 = 5
 
cmd = 3
 
match cmd:
    case Consts.CMD_3:
        print("3")
    case Consts.CMD_5:
        print("5")


                        # На выходе функция должна выдавать или кортеж, или значение None

def book_to_tuple(data: dict | tuple | list, min_year=1800, max_year=3000) -> tuple | None:
    price = None # выносим None за пределы math чтобы не дублировать код
    match data:
        case author, title, int(year):
            pass
        case author, title, int(year), price, *_:
            pass
        case {'author': author, 'title': title, 'year': int(year), 'price': price}: # проверку на большее количество ключей определяем первой
            pass
        case {'author': author, 'title': title, 'year': int(year)}:
            pass
        case _:  # wildcard
            return None
 
    if not (min_year < year < max_year): # выносим условие, чтобы не дублировать код
        return None
 
    return author, title, year, price


                                        # выполним проверку данных в запросе request и вернем результат подключения

def connect_db(connect: dict) -> str:
    match connect:
        case {'server': host, 'login': login, 'password': psw, 'port': port}:
            pass
        case {'server': host, 'login': login, 'password': psw}:
            port = 22
        case _:  # wildcard
            return "error connection"
 
    return f"connection: {host}@{login}.{psw}:{port}"

    