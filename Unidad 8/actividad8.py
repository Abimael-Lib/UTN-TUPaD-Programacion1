try:
    with open("productos.txt", "r") as f:
        pass
except:
    with open("productos.txt", "w") as f:
        f.write("Lapicera,120.5,30\n")
        f.write("Cuaderno,350.0,15\n")
        f.write("Goma,80.0,50\n")


# 2. Leer y mostrar productos + cargarlos en una lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip().split(",")

        nombre = linea[0]
        precio = float(linea[1])
        cantidad = int(linea[2])

        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

        productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })

print("-" * 30)


# 3. Agregar producto ingresado desde teclado
nuevo = input("Ingrese nombre, precio y cantidad (separados por coma): ")

nuevo = nuevo.strip().split(",")

productos.append({
    "nombre": nuevo[0],
    "precio": float(nuevo[1]),
    "cantidad": int(nuevo[2])
})


# 5. Buscar producto por nombre
buscar = input("Ingrese el nombre del producto a buscar: ").strip()

encontrado = False
for p in productos:
    if p["nombre"].lower() == buscar.lower():
        print(f"\nProducto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\n Ese producto no existe.")


# 6. Guardar los productos actualizados sobrescribiendo el archivo
with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\n✔ Archivo actualizado correctamente.")


    








