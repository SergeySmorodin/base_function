                    # Используя list comprehension (генератора списков) 

# Sample Input: 5.56, -8.7, 1.0, 3.14, 77.845 
# Sample Output: [5.56, 8.7, 1.0, 3.14, 77.845]
lst_abs = [abs(float(i)) for i in input().split()] # получение списка по модулю 
print(lst_abs)


# Sample Input: 4567397
# Sample Output: [4, 5, 6, 7, 3, 9, 7]
lst = [int(i) for i in input()]
print(lst)


# Sample Input: Казань Уфа Москва Челябинск Омск Тур Самара
# Sample Output: Казань Москва Челябинск Самара
lst = [i for i in input().split() if len(i) > 5]     # список из названий городов длиной более пяти символов
print(*lst)



                            # НАЙТИ ДЕЛИТЕЛИ ЧИСЛА n

# Необходимо сформировать список с помощью list comprehension, 
# состоящий из делителей числа n (включая и само число n). 
# Ликбез: делителями числа n называются целые числа, которые делят n нацело (без остатка).

# Sample Input: 10
# Sample Output: 1 2 5 10
n = 10
lst = [i for i in range(1, n+1) if n % i == 0]
print(*lst)


                    # СФОРМИРУЙТЕ ДВУМЕРНЫЙ СПИСОК РАЗМЕРНОСТЬЮ N x N

# сформируйте двумерный список размером N x N, состоящий из нулей, а по главной диагонали - единицы. 
# (Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего 

# Sample Input:   4
# Sample Output:  1 0 0 0
#                 0 1 0 0
#                 0 0 1 0
#                 0 0 0 1
N = 5

lst = [[0]*N for i in range(N)] # создаем двумерный список из 0

for i in range(len(lst)):
    lst[i][i] = 1 # меняем 0 на 1 по диагонали
    print(*lst[i])
print()

# используя list comprehension c вложенным циклом
lst = [[0 if i!= j else 1 for j in range(N)] for i in range(N)]    
for i in lst:
    print(*i)


                    # СФОРМИРУЙТЕ ДВУМЕРНЫЙ СПИСОК РАЗМЕРНОСТЬЮ N x N

# Sample Input:       4
# Sample Output:      0 0 0 0
#                     1 1 1 1
#                     2 2 2 2
#                     3 3 3 3
n = 4

lst = [[i] * n for i in range(n)]
for i in lst:
    print(*i)

lst = [(print(*[i] * n)) for i in range(0, n)] # print вложен в генератор


                    # Cформировать список, состоящий из элементов исходного списка, имеющих четные индексы 

# Sample Input:      8.5 11.3 1.0 -4.5 11.34 6.45
# Sample Output:     8.5 1.0 11.34
lst = [float(i) for i in input().split()[::2]]      
print(*lst)

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

