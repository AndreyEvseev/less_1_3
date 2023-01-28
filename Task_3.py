def check_zero():
    y = 0
    while y == 0:
        y = float(input('Введите координату Y, отличную от "0", Y = '))
    return y

def check_quarter(x, y):
    if x > 0 and y > 0:
        print(f'{x= }, {y= } -> точка в 1-й четверти.')
    elif x > 0 and y < 0:
        print(f'{x= }, {y= } -> точка во 2-й четверти.')
    elif x < 0 and y < 0:
        print(f'{x= }, {y= } -> точка в 3-й четверти.')
    else:
        print(f'{x= }, {y= } -> точка в 4-й четверти.')

def check_axis(x, y):
    if x == 0:
        print(f'{x= }, {y= } -> точка на оси "X".')
    else:
        print(f'{x= }, {y= } -> точка на оси "Y".')

x = float(input('Координата X = '))
if x == 0:
    y = check_zero()
else:
    y = float(input('Координата Y = '))
if x == 0 or y == 0:
    check_axis(x, y)
else:
    check_quarter(x, y)
