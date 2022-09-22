import math
age = int(input('Введите возраст поситителя '))
sum = 0
while age != '':
    if age > 3 and age < 12:
        sum += 14
    elif age > 65:
        sum += 18.00
    elif age > 12 and age < 65:
        sum += 23.00
    age = input("Введите возраст поситителя ")
print(round(sum, 2))
