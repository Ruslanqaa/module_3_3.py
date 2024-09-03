def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с разным количеством аргументов
print_params()                # Без аргументов
print_params(b=25)           # Только с изменённым b
print_params(c=[1, 2, 3])    # Только с изменённым c

# 2. Распаковка параметров
values_list = [3.14, 'Текст', False]
values_dict = {'a': 42, 'b': 'Слово', 'c': None}

print_params(*values_list)   # Распаковка списка
print_params(**values_dict)   # Распаковка словаря

# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # Распаковка и отдельный параметр