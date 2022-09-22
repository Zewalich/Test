from math import pi
from math import tan
len = int(input('Введите длину стороны ')) #просим ввести длину стороны
amount = int(input('Введите количество сторон ')) #просим ввести количетсво сторон
area = (amount*len**2)/(4*(tan(pi/amount))) #высчитываем площадь
print(area) #выводим площадь на экран