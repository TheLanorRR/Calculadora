def Potencia(a, b):
    return a ** b

def Modulo(a, b):
    if b == 0:
        return "Error: No se puede calcular el módulo con divisor cero."
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

def Promedio(a):
    if not a:
        return 0
    return sum(a) / len(a)

def Redondeo(a):
    return round(a)

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese un número válido.")
