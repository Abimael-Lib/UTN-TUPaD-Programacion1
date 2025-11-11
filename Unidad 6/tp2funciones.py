# 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2
def saludar_usuario():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola, {nombre}.")

# 3
def informacion_personal():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4
def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    area = 3.14 * (radio ** 2)
    print(f"El área del círculo es {area}.")

def calcular_perimetro_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    perimetro = 2 * 3.14 * radio
    print(f"El perímetro del círculo es {perimetro}.")

# 5
def segundos_a_horas():
    segundos = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos / 3600
    print(f"La cantidad de horas es {horas}.")

# 6
def tabla_multiplicar():
    numero = int(input("Ingrese un número: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7
def operaciones_basicas():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    resultados = (suma, resta, multiplicacion, division)
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")
    print(f"Tupla de resultados: {resultados}")

# 8
def calcular_imc():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = peso / (altura ** 2)
    print(f"Su IMC es {imc}")

# 9
def celsius_a_farenheit():
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    farenheit = (celsius * 9/5) + 32
    print(f"El equivalente en Fahrenheit es {farenheit}")

# 10
def calcular_promedio():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))

    promedio = (a + b + c) / 3
    print(f"El promedio de a, b y c es {promedio}")


imprimir_hola_mundo()
saludar_usuario()
informacion_personal()
calcular_area_circulo()
calcular_perimetro_circulo()
segundos_a_horas()
tabla_multiplicar()
operaciones_basicas()
calcular_imc()
celsius_a_farenheit()
calcular_promedio()

