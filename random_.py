# В программе инициализируется двумерное игровое поле размером N x N 
# (N - натуральное число читается из входного потока), представленное в виде вложенного списка:

# P = [[0] * N for i in range(N)]
# Требуется расставить на поле P случайным образом M = 10 единиц (целочисленных) так, 
# чтобы они не соприкасались друг с другом (то есть, вокруг каждой единицы должны быть нули, либо граница поля). 


import random
random.seed(1)


def is_valid_position(P, row, col):
    # Проверяем ячейку и соседние ячейки
    if P[row][col] == 1:  # Проверяем, занята ли ячейка
        return False

    # Проверяем соседние ячейки
    for i in range(-1, 2):  # Соседи по вертикали
        for j in range(-1, 2):  # Соседи по горизонтали
            if 0 <= row + i < len(P) and 0 <= col + j < len(P):
                if P[row + i][col + j] == 1:
                    return False
    return True


def place_units(P, M):
    N = len(P)
    placed_units = 0

    while placed_units < M:
        row = random.randint(0, N - 1)
        col = random.randint(0, N - 1)
        if is_valid_position(P, row, col):
            P[row][col] = 1
            placed_units += 1


def print_field(P):
    for row in P:
        print(' '.join(map(str, row)))


# Чтение размера поля N
N = int(input("Введите размер поля N: "))

# Инициализация поля
P = [[0] * N for _ in range(N)]

# Количество единиц
M = 10

# Расстановка единиц
place_units(P, M)

# Вывод результата
print_field(P)
