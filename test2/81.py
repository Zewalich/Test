num = (input('Введите число в двоичном виде '  ))  # просим ввести пользователя число в двоичной СС
result = 0  # инициализиурем переменой значение 0
for i in range(len(num)):  # задаем цикл для значения в промежутке равном длине числа
    degree = 2 ** (
                len(num) - i - 1)  # присваеваем переменую, возведения основания двоичного числа в степень равную длине числа
    # минус значение и минус еденица(условия перевода из двоичной СС в десятичную)

    result += int(num[
                      i]) * degree  # переводим двоичное число в десятичное по формуле исходя из правил перевода из двоичной СС в десятичную
print(result)  # выводим на экран результат
