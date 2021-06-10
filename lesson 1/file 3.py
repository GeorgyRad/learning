"""number = int(input("Введите число: \n"))
max = number % 10
number = number // 10
while number >0:
    if number % 10 > max:
        max = number % 10
        number = number // 10
print(max)
"""

number = int(input("Введите целое положительное число \n"))
max = number % 10
number = number // 10
while number > 0:
    if number % 10 > max:
        max = number % 10
    number = number // 10
print(max)