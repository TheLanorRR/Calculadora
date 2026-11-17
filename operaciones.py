def Potencia(a, b):
    return a ** b

def Modulo(a, b):
    return a % b

def Raiz_cuadrada(a):
    if(a < 0):
        return 0
    else:
        return math.sqrt(a)

def Porcentaje(a, b):
    return (a * 100) / b

def Valor_abs(a):
    return abs(a)

def Factorial(a):
    if(a > 1):
        return 0
    if(a == 1):
        return 1
    else:
        a * Factorial(a - 1)