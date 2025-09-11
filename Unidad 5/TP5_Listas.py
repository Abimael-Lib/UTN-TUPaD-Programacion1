# 1
notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
promedio_notas = 0
nota_alta = 0
nota_baja = 100

for i in notas:
    print(i)
    promedio_notas += i
    if nota_alta < i:
        nota_alta = i
    if nota_baja > i:
        nota_baja = i

print(f"El promedio de las notas es de: {promedio_notas / len(notas)}")
print(f"La nota mas alta es de: {nota_alta} y la nota mas baja es de: {nota_baja}")


# 2

productos = []

for i in range(5):
    productos.append(input(f"Ingrese el producto n° {i + 1} por favor: "))
print(sorted(productos))

eliminar = input("Que producto desea eliminar?: ")
productos.remove(eliminar)

actualizar = input("Que producto desea actualizar?: ")
if actualizar in productos:
    indice = productos.index(actualizar)
    productos[indice] = input("Ingrese el nuevo producto: ")

print(productos)

# 3

import random

lista_15_numeros = []
pares = []
impares = []


for i in range(15):
    lista_15_numeros.append(random.randint(1, 100))
print(f"Lista completa de 15 numeros: {lista_15_numeros} \n")

for i in range(15):
    if lista_15_numeros[i] % 2 == 0:
        pares.append(lista_15_numeros[i])
    else:
        impares.append(lista_15_numeros[i])

print(f"Lista de pares: {pares} \n")
print(f"Lista de impares: {impares}")

# 4

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista_sin_repetidos = []

for i in datos:
    if i not in lista_sin_repetidos:
        lista_sin_repetidos.append(i)
    else:
        pass
print(f"Lista sin valores repetidos: {lista_sin_repetidos}")


# 5

estudiantes = ["Juan", "Pedro", "Maria", "Luis", "Ana", "Sofia", "Luisa", "Mario"]

print(f"Estudiantes presentes en clase: {estudiantes}")

respuesta = input("Desea agregar un nuevo estudiante o eliminar uno existente(A/E):")
respuesta = respuesta.lower()
if respuesta == "a":
    estudiantes.append(input("Ingrese el nombre del nuevo estudiante:"))
    print(f"Estudiantes presentes en clase: {estudiantes}")
elif respuesta == "e":
    estudiantes.remove(input("Ingrese el nombre del estudiante a eliminar:"))
    print(f"Estudiantes presentes en clase: {estudiantes}")

# 6

numeros = [2, 3, 5, 6, 1, 7, 15]

numeros = numeros[::-1]
print(numeros)

# 7

temperaturas = [[2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 16], [9, 13]]

promedio_minimas = 0
promedio_maximas = 0
cant_temp = 0

for i in temperaturas:
    promedio_minimas += i[0]
    promedio_maximas += i[1]
    cant_temp += 1

print(f"La temperatura minima pormedio es de: {promedio_minimas / cant_temp}")
print(f"La temperatura maxima pormedio es de: {promedio_maximas / cant_temp}")


# 8

notas_estudiantes = [[3, 5, 8], [4, 6, 9], [5, 7, 10], [6, 8, 11], [7, 9, 12]]

# --- Promedios por estudiante ---
promedios_estudiantes = []

for i in range(len(notas_estudiantes)):
    suma = 0
    for j in range(len(notas_estudiantes[i])):
        suma += notas_estudiantes[i][j]
    promedio = suma / len(notas_estudiantes[i])
    promedios_estudiantes.append(promedio)

for i in range(len(promedios_estudiantes)):
    print(f"El promedio del estudiante {i+1} es de {promedios_estudiantes[i]:.2f}")

# --- Promedios por materia ---
suma_matematicas = 0
suma_fisica = 0
suma_quimica = 0

for i in range(len(notas_estudiantes)):
    suma_matematicas += notas_estudiantes[i][0]
    suma_fisica += notas_estudiantes[i][1]
    suma_quimica += notas_estudiantes[i][2]

promedio_matematicas = suma_matematicas / len(notas_estudiantes)
promedio_fisica = suma_fisica / len(notas_estudiantes)
promedio_quimica = suma_quimica / len(notas_estudiantes)

print(f"El promedio de Matemáticas es de {promedio_matematicas:.2f}")
print(f"El promedio de Física es de {promedio_fisica:.2f}")
print(f"El promedio de Química es de {promedio_quimica:.2f}")


# 9
tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

turno = "X"

for _ in range(9):
    # Mostrar tablero
    print(tablero[0][0], tablero[0][1], tablero[0][2])
    print(tablero[1][0], tablero[1][1], tablero[1][2])
    print(tablero[2][0], tablero[2][1], tablero[2][2])
    print()

    print(f"Turno del jugador {turno}")

    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))

    # Validar que esté dentro del tablero
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Fila o columna inválida. Intente nuevamente.")
        continue

    # Validar si la casilla está vacía
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = turno

        # Cambiar turno usando if normal
        if turno == "X":
            turno = "O"
        else:
            turno = "X"

    else:
        print("Casilla ocupada, intente otra vez.")
        continue

# Mostrar tablero final
print(tablero[0][0], tablero[0][1], tablero[0][2])
print(tablero[1][0], tablero[1][1], tablero[1][2])
print(tablero[2][0], tablero[2][1], tablero[2][2])
print("Fin del juego")


# 10

ventas = [
    [5, 3, 4, 2, 6, 7, 5],
    [2, 4, 3, 5, 3, 2, 4],
    [1, 2, 2, 3, 2, 1, 2],
    [3, 2, 4, 3, 5, 4, 3],
]

productos = ["Detergente", "Jabon", "Esponja", "Escoba"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("Total vendido por producto:")
totales_productos = []
for i in range(4):
    total = 0
    for j in range(7):
        total += ventas[i][j]
    totales_productos.append(total)
    print(f"{productos[i]}: {total}")

totales_dias = []
for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia += ventas[i][j]
    totales_dias.append(total_dia)

max_ventas = totales_dias[0]
dia_max = 0
for j in range(1, 7):
    if totales_dias[j] > max_ventas:
        max_ventas = totales_dias[j]
        dia_max = j
print(
    f"\nEl día con mayores ventas totales fue {dias[dia_max]} con {max_ventas} ventas."
)

max_producto = totales_productos[0]
indice_max_producto = 0
for i in range(1, 4):
    if totales_productos[i] > max_producto:
        max_producto = totales_productos[i]
        indice_max_producto = i
print(
    f"El producto más vendido en la semana fue {productos[indice_max_producto]} con {max_producto} unidades."
)
