# Python Operators: A Quick Guide with Examples

## 1. **Arithmetic Operators**

Python supports basic arithmetic operations:

- **Addition (`+`)**  
  Suma de dos números.  
  ```python
  5 + 3  # 8
Subtraction (-)
Resta entre dos números.
10 - 4  # 6
Multiplication (*)
Multiplicación de dos números.
6 * 2  # 12
Division (/)
División entre dos números (siempre retorna un float).
7 / 2  # 3.5
Floor Division (//)
División entre dos números, redondeando hacia abajo al entero más cercano.
7 // 2  # 3
Modulus (%)
Resto de la división entre dos números.
10 % 3  # 1
Exponentiation (**)
Potenciación de un número.
2 ** 3  # 8

## 2. More Operators
```
Comparison Operators (Return True or False)
5 > 3 → True
4 < 2 → False
10 >= 10 → True
3 <= 2 → False
7 == 7 → True
6 != 5 → True
```
Estos operadores se utilizan para comparar valores y retornan un valor booleano (True o False).

## 3. Shorthand Operators (Augmented Assignment)
```
En lugar de escribir x = x + 5, Python permite usar operadores abreviados para realizar la misma operación:
x = 10
x += 5  # Equivalent to x = x + 5
x -= 2  # Equivalent to x = x - 2
x *= 3  # Equivalent to x = x * 3
x /= 4  # Equivalent to x = x / 4
x //= 2  # Equivalent to x = x // 2
x **= 2  # Equivalent to x = x ** 2
x %= 3  # Equivalent to x = x % 3
```

## 4. Boolean OR (or)

Devuelve True si al menos una de las condiciones es True.
Deja de verificar después del primer True (esto se llama short-circuiting).
```
print(True or False)  # True
print(False or False)  # False
print(5 > 3 or 2 > 10)  # True (since 5 > 3)
| 1 | 1 = 1 | |---|---|---| | 1 | 0 = 1 | | 0 | 1 = 1 | | 0 | 0 = 0 |
```

## 5. Boolean AND (and)

Devuelve True solo si ambas condiciones son True.
Deja de verificar después del primer False (esto también es short-circuiting).
```
print(True and False)  # False
print(4 > 2 and 10 < 20)  # True
print(3 < 1 and 5 > 2)  # False (since 3 < 1 is False)
```
| 1 | 1 = 1 | |---|---|---| | 1 | 0 = 0 | | 0 | 1 = 0 | | 0 | 0 = 0 |

## 6. Boolean Negation (not)

Invierte el valor booleano.

```
print(not True)  # False
print(not False)  # True
print(not (5 > 3))  # False (since 5 > 3 is True, but `not` reverses it)
```

Este archivo `.md` contiene ejemplos prácticos de operadores básicos en Python, incluyendo operadores aritméticos, de comparación, de asignación abreviada y operadores lógicos como `and`, `or` y `not`.



