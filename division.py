number_1 = int(input("первое число: "))
operation = input("действие (+, -, *, /): ")
number_2 = int(input("второе число: "))

if operation == "+":
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "*":
    result = number_1 * number_2
elif operation == "/":
    if number_2 != 0:
        result = number_1 / number_2
    else:
        result = "Ошибка: будет бесконечность!"
else:
    result = "Неизвестная операция"

print("результат", result)

