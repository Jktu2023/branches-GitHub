
def priamoug(a, b):
    s = a * b
    print(f'Площадь прямоугольника равна: {s}')

def triug(a, b):
    s = a * b / 2
    print(f'Площадь треугольника равна: {s}')

def trap(a, b, h):
    s = (a + b) / 2 * h
    print(f'Площадь трапеции равна: {s}')


a  = float(input('введите сторону 1 - '))
b = float(input('введите сторону 2 - '))
h = input('высота будет (если нет Enter) - ')
try:
    h = float(h)
except:
    pass


print('выбирите фигуру площадь которой хотите подсчитать:\n1 - прямоугольник.\n2 - примоугольный треугольник.\n3 - трпеция.')
choise = input('итак: ')
print()
if choise == '1':
    priamoug(a, b)
elif choise == '2':
    triug(a, b)
elif choise == '3':
    try:
        trap(a, b, h)
    except:
        print('Вы высоту трапеции указывали?')



