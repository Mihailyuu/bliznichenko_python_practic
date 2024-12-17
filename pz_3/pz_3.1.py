# Дано целое число А. Проверить истинность высказывания: «Число А является четным».

A = input('Введите целое число: ')

# Проверка, является ли введенное значение целым числом
while type(A) != int:
    try:
        A = int(A)  # Попытка преобразовать введенное значение в целое число
    except ValueError:
        print('Неправильно ввели!')
        A = input('Введите целое число: ')

# Проверка четности числа
if A % 2 == 0:
    print("True")  # Число четное
else:
    print("False")  # Число нечетное