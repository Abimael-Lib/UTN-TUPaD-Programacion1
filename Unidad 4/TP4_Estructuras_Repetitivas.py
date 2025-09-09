# 1
for i in range(101):
    print(i)


# 2
numero = int(input("Ingrese un numero: "))
cant_digitos = 0
for i in str(numero):
    cant_digitos += len(str(i))
print(cant_digitos)


# 3
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

suma_nums = 0
for i in range(num1 + 1, num2):
    suma_nums += i
print(suma_nums)


# 4
numer = int(input("Ingrese un número: "))

suma = 0
while numer != 0:
    suma += numer
    numer = int(input("Ingrese un número: "))
print(suma)


# 5
import random

nummer = int(input("Ingrese un número: "))
contador = 0
while nummer != random.randint(1, 9):
    contador += 1
    nummer = int(input("Ingrese un número: "))

print(f"Adivinaste el número en {contador} intentos")


# 6
cont = 100
while cont > 0:
    if cont % 2 == 0:
        print(cont)
    cont = cont - 1

# 7
numero_mayor = int(input("Ingrese un número: "))
sumatoria = 0
for i in range(numero_mayor):
    sumatoria += i
print(sumatoria)

# 8
intentos = 0
pares = 0
impares = 0
negativos = 0
positivos = 0

while intentos < 100:
    nums_100 = int(input("Ingrese un número: "))
    intentos += 1
    if nums_100 % 2 == 0:
        pares += 1
    else:
        impares += 1

    if nums_100 < 0:
        negativos += 1
    else:
        positivos += 1
print(f"La cantidad de pares es de: {pares}")
print(f"La cantidad de impares es de: {impares}")
print(f"La cantidad de negativos es de: {negativos}")
print(f"La cantidad de positivos es de: {positivos}")


# 9
intentos = 0
sumatoria = 0
media = 0

while intentos < 100:
    nums_100 = int(input("Ingrese un número: "))
    intentos += 1
    sumatoria += nums_100
    media = sumatoria / intentos
print(f"La media es de: {media}")


# 10
numero_entero = int(input("Ingrese un número entero: "))

print(int(str(numero_entero)[::-1]))
