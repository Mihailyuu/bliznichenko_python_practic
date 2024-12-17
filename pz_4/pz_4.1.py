# Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг конфет.

sweet_price = float(input("Введите цену 1 кг конфет: "))
amount_sweet = 1
cost_sweet = 0

# Проверка корректности ввода цены
while type(sweet_price) != float:
    try:
        sweet_price = float(sweet_price)
    except ValueError:
        print("Некорректно введены данные")
        sweet_price = float(input("Введите цену 1 кг конфет: "))

# Вычисление стоимости конфет для каждого количества от 1 до 10 кг
while amount_sweet <= 10:
    cost_sweet = sweet_price * amount_sweet
    print(cost_sweet, end=" ")
    amount_sweet += 1