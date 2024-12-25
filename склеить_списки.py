                     # Собрать список из городов и числинности населения

# Sample Input:  Москва 15000 Уфа 1200 Самара 1090 Казань 1300
# Sample Output: [['Москва', 15000], ['Уфа', 1200], ['Самара', 1090], ['Казань', 1300]]
lst = ['Москва', 15000, 'Уфа', 1200, 'Самара', 1090, 'Казань', 1300]

result_city = [str(lst[i]) for i in range(0, len(lst), 2)] # создаем список городов, используя шаг 2 от 0 индекса
result_digit = [int(lst[i]) for i in range(1, len(lst), 2)] # создаем список городов, используя шаг 2 от 1 индекса
result = [[result_city[i], result_digit[i]] for i in range(len(result_city))] # создаем список в списке
print(result)

# решение в 1 строку
cities  = ['Москва', 15000, 'Уфа', 1200, 'Самара', 1090, 'Казань', 1300]
lst = [[cities[i], int(cities[i+1])] for i in range(0, len(cities), 2)] # сразу используем индексы общего списка
print(lst)

                    # Определить сумму соответствующих пар чисел введенных списков

# Sample Input:   1 2 3 4 5
#                 6 7 8 9 10
# Sample Output:  7 9 11 13 15

# lst_1 = [int(i) for i in input().split()]
# lst_2 = [int(i) for i in input().split()]
lst_1 = [1, 2, 3, 4, 5]
lst_2 = [6, 7, 8, 9, 10]

lst_3 = [lst_1[i] + lst_2[i] for i in range(len(lst_1))]
print(lst_3)

