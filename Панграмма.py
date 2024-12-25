# Панграмма — это предложение, которое содержит все буквы алфавита
# хотя бы один раз.


alpha = 'abcdefghijklmnopqrstuvwxyz'
chars_to_remove = ",!. "


# решение 1
def is_pangram(string):
    s = string.lower()
    for char in chars_to_remove:
        s = s.replace(char, "")  # Обновляем s на каждом шаге
    return set(s) >= set(alpha)  # Проверяем, содержатся ли все буквы


print(is_pangram("The quick brown fox jumps over the lazy dog!!!!."))


# решение 2
def is_pangram(string):
    translation_table = str.maketrans('', '', chars_to_remove)
    cleaned_string = string.translate(translation_table).lower()
    return set(cleaned_string) >= set(alpha)


print(is_pangram("The quick brown fox jumps over the lazy dog!!!!."))


# решение 3
def is_pangram(string):
    s = ''.join(
        [char for char in string.lower() if char not in chars_to_remove]
    )
    return set(s) >= set(alpha)


# решение 4
def is_pangram(s, alpha='abcdefghijklmnopqrstuvwxyz'):
    return set(alpha).issubset(set(s.lower()))


# решение 5
def is_pangram(s):
    return {i for i in s.lower() if i.isalpha()} == set(alpha)


# решение 6
def is_pangram(s):
    return sum(1 for _ in alpha if _ in s.lower()) == 26
