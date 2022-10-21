figure = int(input("Введите число:"))
system = int(input("Введите целевую систему счисления (2 или 8):"))

def translation(figure, system):
    result = ''
    if system == 2:
        while figure > 0:
            result = str(figure % 2) + result
            figure = figure // 2 
        print(result)
    elif system == 8:
        while figure > 0:
            result = str(figure % 8) + result 
            figure = figure // 8
        print(result)
    else:
        print("Ошибка: введите одно из предложенных оснований систем счисления")

translation(figure, system)