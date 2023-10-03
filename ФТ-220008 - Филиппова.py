# Задание 1

a=float(input('Введите первое число: '))
b=float(input('Введите второе число: '))


I=[a+b, a-b, a*b,  round((a+b)/2, 2)]
I1 = ["Сумма: ", "Разность: ", "Произведение: ", "Среднее арифметическое: "]
for i in range(4):
	print (I1[i], I[i])

def mod(x):
    if x < 0:
        x = -x
    return x

def razn(x,y):
    x = mod(x)
    y = mod(y)
    max_xy = x
    min_xy = y

    if x < y:
        max_xy = y
        min_xy = x
    else:
        None

    return max_xy - min_xy

print("Разность минимального и максимального по модулю: ", razn(a,b))













