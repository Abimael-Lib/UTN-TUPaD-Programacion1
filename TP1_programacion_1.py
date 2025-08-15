# Problema 1
def hola_mundo():
    return "Hola Mundo!"


# Problema 2
def saludo():
    nombre = input()
    print(f"Hola {nombre}!")


# Problema 3
def oracion_datos():
    nombre = input()
    apellido = input()
    edad = int(input())
    pais = input()
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}.")


# Problema 4
def area_y_perimetro():
    radio = float(input())

    area = 3.14 * (radio**2)
    perimetro = 2 * 3.14 * radio
    print(f"El area es de {area} y el perimetro es de {perimetro}.")


# Problema 5
def segundos_a_horas():
    segundos = int(input())
    horas = segundos // 60 // 60
    print(f"{segundos} segundos equivalen a {horas} horas")


# Problema 6
def tabla_multiplicar_numero():
    numero = int(input())
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(i * numero)


# Problema 7
def dos_numeros():
    num1 = int(input("Ingrese el primer número distinto de cero: "))
    num1 = int(input("Ingrese el segundo número distinto de cero: "))
    if num1 == 0:
        num1 = int(input("El primer número es 0, ingrese nuevamente: "))
    elif num2 == 0:
        num2 = int(input("El segundo número es 0, ingrese nuevamente: "))
    else:
        pass

    print(f"{num1} sumado a {num2} es: {num1 + num2}")
    print(f"{num1} dividido por {num2} es: {num1 // num2}")
    print(f"{num1} multiplicado por {num2} es: {num1 * num2}")
    print(f"{num1} menos {num2} es: {num1 - num2}")


# Problema 8
def indice_masa_corporal():
    altura = float(input("Ingrese su altura en metros: "))
    peso = float(input("Ingrese su pero en kilogramos: "))
    imc = peso / altura**2
    print(f"Su indice de masa corporal(IMC) es de: {imc}")


# Problema 9
def celsius_a_fahrenheit():
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (9 / 5) * celsius + 32

    print(f"La temperatura en grados Fahrenheit es de: {fahrenheit}")


# Problema 10
def promedio_de_tres():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    promedio = (num1 + num2 + num3) / 3
    print(f"El promedio de los 3 números es de: {promedio}")
