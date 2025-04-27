number = int(input("Суйчас отзеркалит : "))
fifth = number % 10
fourth = (number % 100) // 10
third = (number % 1000) // 100
second = (number % 10000) // 1000
first = (number % 100000) // 10000
reversed_number = fifth * 10000 + fourth * 1000 + third * 100 + second * 10 + first
print(reversed_number)
