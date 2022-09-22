import math
sum = int(input('сумма заказа в ресторане ')) #просим ввести сумму заказа
tips = sum*0.18 #высчитываем чаевые
tax = sum*0.2 #высчитываем налог
print('tax =', round(tax, 2), 'tips =', round(tips, 2), "sum = ", round(sum-tax-tips, 2)) #выводим налог,чаевые и сумму после их вычеты
