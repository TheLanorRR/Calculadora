from operaciones import (
    Potencia, Modulo, Raiz_cuadrada, Porcentaje, 
    Valor_abs, Factorial, Promedio, Redondeo
)

def mostrar_menu():
    """Muestra el menú principal con las operaciones disponibles."""
    print("\n==================================")
    print("      CALCULADORA PYTHON FNI      ")
    print("==================================")
    print(" 1. Potencia")
    print(" 2. Módulo")
    print(" 3. Raíz cuadrada")
    print(" 4. Porcentaje")
    print(" 5. Valor absoluto")
    print(" 6. Factorial")
    print(" 7. Promedio")
    print(" 8. Redondeo")
    print(" 0. Salir")
    print("==================================")

def pedir_numero(mensaje):
    """Valida entradas numéricas (Problema 9)."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Entrada no válida. Por favor, ingrese un número.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("\n¡Saliendo de la calculadora. Hasta luego!")
            break

        if opcion == "1":
            base = pedir_numero("Ingrese la base: ")
            exp = pedir_numero("Ingrese el exponente: ")
            print(f"Resultado: {Potencia(base, exp)}")

        elif opcion == "2":
            a = pedir_numero("Ingrese el dividendo: ")
            b = pedir_numero("Ingrese el divisor: ")
            # Control de división por cero (Problema 10)
            if b == 0:
                print("❌ Error: No se puede calcular el módulo con divisor cero.")
            else:
                print(f"Resultado: {Modulo(a, b)}")

        elif opcion == "3":
            a = pedir_numero("Ingrese el número: ")
            if a < 0:
                print("❌ Error: No se puede calcular la raíz cuadrada de un número negativo.")
            else:
                print(f"Resultado: {Raiz_cuadrada(a)}")

        elif opcion == "4":
            cant = pedir_numero("Ingrese la cantidad total: ")
            porc = pedir_numero("Ingrese el porcentaje a calcular: ")
            print(f"Resultado: {Porcentaje(cant, porc)}")

        elif opcion == "5":
            a = pedir_numero("Ingrese el número: ")
            print(f"Resultado: {Valor_abs(a)}")

        elif opcion == "6":
            a = int(pedir_numero("Ingrese un número entero no negativo: "))
            if a < 0:
                print("❌ Error: El factorial no está definido para negativos.")
            else:
                print(f"Resultado: {Factorial(a)}")

        elif opcion == "7":
            print("Ingrese los números separados por espacio:")
            entrada = input("-> ")
            try:
                numeros = [float(x) for x in entrada.split()]
                if not numeros:
                    print("❌ Error: Debe ingresar al menos un número.")
                else:
                    print(f"Resultado: {Promedio(numeros)}")
            except ValueError:
                print("❌ Error: Todos los valores deben ser numéricos.")

        elif opcion == "8":
            val = pedir_numero("Ingrese el número con decimales: ")
            dec = int(pedir_numero("Ingrese la cantidad de decimales deseada: "))
            print(f"Resultado: {Redondeo(val, dec)}")

        else:
            print("❌ Opción no válida. Por favor, elija una opción del menú.")

        print("\nOperación finalizada. Volviendo al menú...")

if __name__ == "__main__":
    main()