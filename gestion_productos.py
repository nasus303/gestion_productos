productos = []

def añadir_producto():
    nombre = input("Ingrese nombre del producto: ")
    while True:
        precio = input("Ingrese precio del producto: ")
        if precio.isdigit() and float(precio) > 0:
            precio = float(precio)
            break
        else:
            print("Ingrese un precio valido")
    while True:
        cantidad = input("Ingrese cantidad del producto: ")
        if cantidad.isdigit() and int(cantidad) >0: 
            cantidad = int(cantidad)
            break
        else:
            print("Ingrese un precio valido")

    productos.append({'producto': nombre, 'precio': precio, 'cantidad': cantidad})

def ver_productos():
    if not productos:
        print("No hay productos")
    else:
        print(productos)

def actualizar_producto():
    producto_nombre = input("Ingrese el nombre del producto a actualizar: ")
    for i in productos:
        if i['producto'].lower() == producto_nombre.lower():
          opc = int(input("Seleccione la opción que desea actualizar: (1) Precio del producto, (2) Cantidad: "))
          if opc == 1:
              while True:
                  precio_actualizar = input("Ingrese el nuevo precio: ")
                  if precio_actualizar.isdigit() and float(precio_actualizar) >0:
                      i['precio'] = float(precio_actualizar)
                      print("Precio actualizado correctamente")
                      return
                  else:
                      print("Ingrese un precio valido")
          elif opc == 2:
              while True:
                  cantidad_actualizar = input("Ingrese la nueva cantidad: ")
                  if cantidad_actualizar.isdigit() and int(cantidad_actualizar) >0:
                      i['cantidad'] = int(cantidad_actualizar)
                      print("Cantidad actualizada correctamente")
                      return
                  else:
                      print("Ingrese una cantidad valida")
          else:
              print("Opción no valida.")
              return
    print("Producto no encontrado")

def eliminar_producto():
    producto_nombre = input("Ingrese el nombre del producto a eliminar: ")
    for i in productos:
        if i['producto'].lower() == producto_nombre.lower():
            productos.remove(i)
            print("Producto eliminado correctamente")
            return
    print("Producto no encontrado")

def guardar_datos():
    with open ("productos.txt", "w") as archivo:
        for i in productos:
            archivo.write(f"{i['producto']},{i['precio']},{i['cantidad']}\n")
    print("Datos guardados")

def cargar_datos():
    try:
        with open('productos.txt', 'r') as archivo:
            for i in archivo:
                nombre, precio, cantidad = i.strip().split(",")
                productos.append({
                    'producto':nombre,
                    'precio':float(precio),
                    'cantidad':int(cantidad)
                })
        print("Datos cargados")
    except FileNotFoundError:
        print("No hay resultados guardados todavía.")
    except Exception as e:
        print(f"Ocurrio un error al cargar los datos: {e}")

def menu():
    cargar_datos()
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()