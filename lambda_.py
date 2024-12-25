get_div = lambda x, y: x / y if y != 0 else None # можно просто if y, равноценно y = True

print(get_div(10, 0))


                # вызовите функцию filter_lst несколько раз для формирования:

# кортежа из всех значений списка digs (передается в параметр it);
# кортежа только из отрицательных чисел переданного списка digs;
# кортежа только из неотрицательных чисел (то есть, включая и 0) переданного списка digs;
# кортежа из чисел в диапазоне [3; 5] переданного списка digs.


# решение 1
def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)
    return res

digs = [int(i) for i in input().split()]

lst = filter_lst(digs)
print(*lst)
lst = filter_lst(digs, lambda x: x < 0)
print(*lst)
lst = filter_lst(digs, lambda x: x >= 0)
print(*lst)
lst = filter_lst(digs, lambda x: 3 <= x <= 5)
print(*lst)


# решение 2
filter_lst = lambda it, key=None: tuple(it if key is None else filter(key, it))

digs = list(map(int, input().split()))
for filter_func in (None, lambda x: x < 0, lambda x: x >= 0, lambda x: 2 < x < 6):
    print(*filter_lst(digs, key=filter_func))


# решение 3
def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

digs = list(map(int, input().split()))
lambda_list = [None, lambda x: x < 0, lambda x: x >= 0, lambda x: 3 <= x <= 5]
for l in lambda_list:
    print(*filter_lst(digs, l))



#   вывести города длиной более 5 символов. Вместо остальных названий - строку с дефисом ("-")  
cities = list(map(lambda x: x if len(x) > 5 else "-", input().split()))



