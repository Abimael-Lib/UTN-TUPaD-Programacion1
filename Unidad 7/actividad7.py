# 1) Añadir frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# 2) Actualizar precios
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# 3) Crear lista solo con las frutas
lista_solo_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_solo_frutas)

# 4) Números de teléfono
numeros_de_telefono = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = int(input("Ingrese el número de teléfono: "))
    numeros_de_telefono[nombre] = numero

consulta = input("Ingrese el nombre que desea consultar: ")
if consulta in numeros_de_telefono:
    print(f"El teléfono de {consulta} es: {numeros_de_telefono[consulta]}")
else:
    print("No se encontró el contacto.")

# 5) Frase y conteo de palabras
frase = input("Dame una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
veces_palabra = {palabra: palabras.count(palabra) for palabra in palabras_unicas}

print("Palabras únicas:", palabras_unicas)
print("Veces que aparece cada palabra:", veces_palabra)

# 6) Alumnos y notas (usando tuplas)
alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(int(input("Ingrese la nota: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

# 7) Sets de estudiantes
set_1 = {"Juan", "Pedro", "Maria", "Luis", "Ana", "Sofia", "Luisa", "Mario"}
set_2 = {"Juan", "Pedro", "Maria", "Maximo", "Lucas", "Carlos", "Mariano"}

print("Aprobaron ambos:", set_1 & set_2)
print("Aprobaron solo uno:", set_1 ^ set_2)
print("Aprobaron al menos uno:", set_1 | set_2)

# 8) Diccionario de productos y stock
productos_stock = {
    "Camisa": 10,
    "Pantalon": 5,
    "Zapatos": 8,
    "Bolso": 15,
    "Gorra": 12,
    "Gafas": 3,
    "Reloj": 6,
}

print("\nElija la opción que desea realizar: ")
print("1. Consultar producto ingresado")
print("2. Agregar unidades al stock")
print("3. Agregar un nuevo producto al stock")
opcion = int(input("Ingrese una opción: "))

if opcion == 1:
    producto = input("Ingrese el producto que desea consultar: ")
    if producto in productos_stock:
        print(f"El producto {producto} tiene {productos_stock[producto]} unidades en stock.")
    else:
        print(f"El producto {producto} no se encuentra en el stock.")
elif opcion == 2:
    producto = input("Ingrese el producto que desea agregar unidades: ")
    if producto in productos_stock:
        unidades = int(input("Ingrese la cantidad de unidades que desea agregar: "))
        productos_stock[producto] += unidades
        print(f"Stock actualizado: {producto} ahora tiene {productos_stock[producto]} unidades.")
    else:
        print(f"El producto {producto} no se encuentra en el stock.")
elif opcion == 3:
    producto = input("Ingrese el producto que desea agregar al stock: ")
    unidades = int(input("Ingrese la cantidad inicial: "))
    productos_stock[producto] = unidades
    print(f"Producto {producto} agregado con {unidades} unidades.")

# 9) Agenda con tuplas (día, hora)
agenda = {
    ("lunes", "10:00"): "Clase de programación",
    ("martes", "10:00"): "Clase de matemáticas",
    ("miércoles", "10:00"): "Clase de física",
    ("jueves", "10:00"): "Clase de química",
    ("viernes", "10:00"): "Clase de inglés",
}

dia = input("Ingrese el día que desea consultar: ")
hora = input("Ingrese la hora (por ejemplo 10:00): ")
clave = (dia, hora)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividad programada en ese horario.")

# 10) Invertir diccionario
original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Colombia": "Bogotá", "Perú": "Lima"}
invertido = {capital: pais for pais, capital in original.items()}
print("Diccionario original:", original)
print("Diccionario invertido:", invertido)
