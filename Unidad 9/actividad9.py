# 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Ingrese un número: "))

for i in range(1, n + 1):
    print(f"Factorial de {i} = {factorial(i)}")

# 2
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingrese la posición: "))

print("Serie de Fibonacci:")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")

# 3
def potencia(n, m):
    if m == 0:
        return 1
    return n * potencia(n, m - 1)

base = int(input("Base: "))
exp = int(input("Exponente: "))

print("Resultado:", potencia(base, exp))

# 4
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(num)
print("Binario:", binario if binario != "" else "0")

# 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ")
print("Es palíndromo:", es_palindromo(texto))

# 6
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingrese un número: "))
print("Suma de dígitos:", suma_digitos(num))

# 7
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

niveles = int(input("Bloques en el nivel más bajo: "))
print("Bloques totales:", contar_bloques(niveles))

# 8
def contar_digito(numero, digito):
    if numero == 0:
        return 1 if digito == 0 else 0
    if numero < 10:
        return 1 if numero == digito else 0
    return contar_digito(numero // 10, digito) + (1 if numero % 10 == digito else 0)

num = int(input("Número: "))
dig = int(input("Dígito a buscar: "))
print("Cantidad:", contar_digito(num, dig))

