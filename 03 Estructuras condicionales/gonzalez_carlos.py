# 1 ------------------------------------------------------------------
edad = int(input("Ingrese su edad por favor: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")


# 2 ------------------------------------------------------------------
nota = int(input("Ingrese su nota:"))

if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprovado.")

# 3 ------------------------------------------------------------------
numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("NPor favor, ingrese un número par")

# 4 ------------------------------------------------------------------

edad1 = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto joven")
elif edad >= 30:
    print("Adulto")

# 5 ------------------------------------------------------------------
contraseña = input("Ingrese su contraseña: ")

if len(contraseña) < 8 or len(contraseña) > 14:
    print("Por favor ingrese una contraseña entre 8 y 14 caracteres.")
else:
    print("Ha ingresado una contraseña correcta.")

# 6 ------------------------------------------------------------------
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana:
    print("Hay un sesgo positivo.")
elif media < mediana:
    print("Hay un sesgo negativo.")
else:
    print("No hay sesgo.")

# 7 ------------------------------------------------------------------
frase = input("Ingrese una frase o palabra: ")

if (
    frase[::-1] == "a"
    or frase[::-1] == "e"
    or frase[::-1] == "i"
    or frase[::-1] == "o"
    or frase[::-1] == "u"
):
    print(frase, "!")
else:
    print(frase)

# 8 ------------------------------------------------------------------
nombre = input("Ingrese su nombre: ")
numero = int(
    input(
        "Ingrese un numero, 1 Nombre en mayusculas, 2 Nombre en minusculas, 3 Nombre con la primera letra en mayuscula: "
    )
)

if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())


# 9 ------------------------------------------------------------------
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print('"Muy leve" (imperceptible).')
elif magnitud >= 3 and magnitud < 4:
    print('"Leve" (ligeramente perceptible).')
elif magnitud >= 4 and magnitud < 5:
    print('"Moderado" (sentido por personas, pero generalmente no causa daños).')
elif magnitud >= 5 and magnitud < 6:
    print('"Fuerte" (puede causar daños en estructuras débiles).')
elif magnitud >= 6 and magnitud < 7:
    print('"Muy fuerte" (puede causar daños significativos).')
elif magnitud >= 7 and magnitud < 8:
    print('"Extremo" (puede causar graves daños a gran escala).')


# 10  -----------------------------------------------------------------

emisferio = input("Ingrese el emisferio Norte o Sur: ")
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el dia: "))

if emisferio == "n":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("Prima")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Verano")
    elif (
        (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20)
    ):
        print("Otono")
else:
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("Otono")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("Verano")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Prima")
    elif (
        (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20)
    ):
        print("Invierno")
