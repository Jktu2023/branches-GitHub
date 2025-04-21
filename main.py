
def priamoug(a, b):
    s = a * b
    print(f'Площадь прямоугольника равна: {s}')
def triug(a, b):
    s = a * b / 2
    print(f'Площадь триугольника равна: {s}')


a  = float(input('введите сторону 1 - '))
b = float(input('введите сторону 2 - '))
print('выбирите фигуру площадь которой хотите подсчитать:\n1 - прямоугольник.\n2 - примоугольный треугольник.')
choise = input('итак: ')
print()
if choise == '1':
    priamoug(a, b)
elif choise == '2':
    triug(a, b)

