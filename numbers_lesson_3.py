some_number = "       3435  "
# ............................................

some_number = some_number.strip()
some_number = int(some_number)


some_number_mult_2 = some_number * 2
print(some_number_mult_2)

number_value = 5_45_4545_454
number_mult = number_value * 5
number_mult *= 2

number_mult /= 4
num1 = 0.1
num2 = 0.2
num3 = num1 + num2

num4 = num1 - num3
negative_number1 = -1
negative_number2 = -156.124
rounded_negative_number2_int = round(negative_number2, 2)
negative_bad_number = -156.0

power = 5**2
root = 25**0.5

div1 = 26 // 5
rest = 26 % 5

hw = 123235
hw_1 = hw // 100_000
hw_2 = (hw - hw_1 * 100_000) // 10_000
reversed_value = hw_2 * 10000 + hw * 10000

pass
