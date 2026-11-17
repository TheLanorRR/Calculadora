# Calculadora de Operaciones

Programa en Python que realiza operaciones matemáticas y **almacena y muestra el historial de las operaciones realizadas durante la ejecución**.

## Características

- Operaciones matemáticas: potencia, módulo, raíz cuadrada, porcentaje, valor absoluto, factorial, promedio y redondeo.
- Validación de entradas numéricas.
- Manejo de errores (división entre cero, números negativos, etc.).
- **Historial de operaciones**: cada operación se guarda en memoria y se puede consultar en cualquier momento mientras el programa esté en ejecución.

## Requisitos

- Python 3.8 o superior
- No requiere librerías externas (solo la biblioteca estándar: `math`)

## Estructura del proyecto

```
.
├── operaciones.py   # Funciones matemáticas y utilidades
└── README.md
```

## Funciones disponibles

| Función | Descripción | Ejemplo |
|---|---|---|
| `Potencia(a, b)` | Eleva `a` a la potencia `b` | `Potencia(2, 3)` → `8` |
| `Modulo(a, b)` | Residuo de `a / b` | `Modulo(10, 3)` → `1` |
| `Raiz_cuadrada(a)` | Raíz cuadrada de `a` | `Raiz_cuadrada(16)` → `4.0` |
| `Porcentaje(a, b)` | Porcentaje que representa `a` de `b` | `Porcentaje(25, 200)` → `12.5` |
| `Valor_abs(a)` | Valor absoluto | `Valor_abs(-7)` → `7` |
| `Factorial(a)` | Factorial de `a` | `Factorial(5)` → `120` |
| `Promedio(lista)` | Promedio de una lista | `Promedio([2, 4, 6])` → `4.0` |
| `Redondeo(a)` | Redondea al entero más cercano | `Redondeo(3.7)` → `4` |
| `pedir_numero(mensaje)` | Pide un número por consola y valida la entrada | — |

## Historial de operaciones

Cada vez que se ejecuta una operación, se registra en una lista en memoria con
la operación, los valores de entrada y el resultado.

- **Almacenamiento:** lista `historial` que se mantiene mientras el programa esté en ejecución.
- **Registro:** `registrar_operacion(nombre, entradas, resultado)` agrega una entrada al historial.
- **Consulta:** `mostrar_historial()` imprime todas las operaciones realizadas.

> El historial **no se guarda en disco**: se pierde al cerrar el programa.

### Ejemplo de salida

```
===== HISTORIAL DE OPERACIONES =====
1. Potencia(2, 3) = 8
2. Modulo(10, 3) = 1
3. Raiz_cuadrada(16) = 4.0
4. Porcentaje(25, 200) = 12.5
====================================
```

Si aún no se ha realizado ninguna operación:

```
No hay operaciones en el historial.
```

## Uso

```bash
python operaciones.py
```

Ejemplo de uso desde código:

```python
from operaciones import *

resultado = Potencia(2, 3)
registrar_operacion("Potencia", (2, 3), resultado)
mostrar_historial()
```

## Manejo de errores

- Entradas no numéricas: se vuelve a pedir el dato.
- Módulo con divisor cero: devuelve un mensaje de error.
- Raíz cuadrada de un número negativo: devuelve `0`.

## Autor

Tu nombre aquí