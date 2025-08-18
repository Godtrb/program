class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre.strip()
        self.categoria = categoria.strip()
        self.precio = float(precio)
        self.stock = stock

    def __str__(self):
        return f"Código: {self.codigo} Producto: {self.nombre} Categoría: {self.categoria}  Precio: {self.precio}  Stock: {self.stock}"


class Inventario:
    def __init__(self):
        self.Productos = {}

    def agregar(self):
        while True:
            while True:
                try:
                    codigo = int(input("Ingrese código del producto: "))
                    if codigo <= 0:
                        print("El código debe ser un número entero positivo.\n")
                        continue
                    if codigo in self.Productos:
                        print("El código ya existe en el inventario.\n")
                        continue
                    break
                except ValueError:
                    print("Debe ingresar un número entero.\n")

            while True:
                nombre = input("Ingrese nombre: ").strip()
                if nombre == "":
                    print("Error: El nombre no puede quedar vacío.\n")
                else:
                    try:
                        int(nombre)
                        print("Error: El nombre no puede ser un número.\n")
                    except ValueError:
                        break

            while True:
                categoria = input("Ingrese categoría: ").strip()
                if categoria == "":
                    print("Error: La categoría no puede quedar vacía.\n")
                else:
                    try:
                        int(categoria)
                        print("Error: La categoría no puede ser un número.\n")
                    except ValueError:
                        break

            while True:
                try:
                    precio = float(input("Ingrese precio: "))
                    if precio <= 0:
                        print("El precio debe ser un número positivo.\n")
                        continue
                    break
                except ValueError:
                    print("Error: Debe ingresar un número válido para el precio.\n")

            while True:
                try:
                    stock = int(input("Ingrese stock: "))
                    if stock < 0:
                        print("Error: El stock debe ser un número entero no negativo.\n")
                        continue
                    break
                except ValueError:
                    print("Error: Debe ingresar un número entero para el stock.\n")

            producto = Producto(codigo, nombre, categoria, precio, stock)
            self.Productos[codigo] = producto
            print("Producto agregado correctamente.\n")

            while True:
                respuesta = input("¿Desea agregar otro producto? (si/no): ").strip().lower()
                if respuesta == "si":
                    break
                elif respuesta == "no":
                    return
                else:
                    print("Opción inválida. Responda 'si' o 'no'.\n")

    def modif(self, codigo):
        try:
                print("¿Qué desea modificar?")
                print("1) Nombre")
                print("2) Categoría")
                print("3) Precio")
                print("4) Stock")
                print("5) Regresar")

                menpick = int(input("Ingresar opción: "))

                if menpick == 1:
                    name = input("Ingrese el nuevo nombre: ")
                    self.Productos[codigo].nombre = name
                    print("Nombre actualizado correctamente.")

                elif menpick == 2:
                    categ = input("Ingrese la nueva categoría: ")
                    self.Productos[codigo].categoria = categ
                    print("Categoría actualizada correctamente.")

                elif menpick == 3:
                    precio = float(input("Ingrese el nuevo precio: "))
                    self.Productos[codigo].precio = precio
                    print("Precio actualizado correctamente.")

                elif menpick == 4:
                    stock = int(input("Ingrese el nuevo stock: "))
                    self.Productos[codigo].stock = stock
                    print("Stock actualizado correctamente.")

                elif menpick == 5:
                    print("Regresando al menú principal...")

                else:
                    print("Opción no válida, intente nuevamente.")

        except ValueError:
            print("Error: Ingrese un valor válido.")
    def modif(self, codigo):
        self.Productos[codigo].pop()
        print("Producto eliminado correctamente.")

class Listado():
    def __init__(self, inventario):
        self.Productos = inventario.Productos

    def quick_sort(self, lista, buscar):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if buscar(x) < buscar(pivote)]
        iguales = [x for x in lista if buscar(x) == buscar(pivote)]
        mayores = [x for x in lista[1:] if buscar(x) > buscar(pivote)]
        return self.quick_sort(menores, buscar) + iguales + self.quick_sort(mayores, buscar)


    def menu_Salida(self):
        while True:
            opcion = input("\n¿Desea regresar al menú principal o salir? (menu/salir): ").strip().lower()
            if opcion == "menu":
                return
            elif opcion == "salir":
                print("Adiós, vuelva pronto.")
                exit()
            else:
                 print("Opción inválida. Responda 'menu' o 'salir'.")

    def ordenamiento(self):
            if not  self.Productos:
                print("Aún no hay productos en el inventario.")
                self.menu_Salida()
                return
            productos_lista = list(self.Productos.values())
            print("\n--- LISTADO DE PRODUCTOS  ---")
            for producto in productos_lista:
                print(producto)
            while True:
                print("\nOrdenar por:")
                print("1) Nombre")
                print("2) Precio")
                print("3) Stock")
                try:
                    opcion = int(input("Seleccione una opción: "))
                except ValueError:
                    print(" Debe ingresar un número válido.\n")
                    continue

                def por_nombre(prod):
                    return prod.nombre.lower()

                def por_precio(prod):
                    return prod.precio

                def por_stock(prod):
                    return prod.stock

                if opcion == 1:
                    productos_lista = self.quick_sort(productos_lista, buscar=por_nombre)
                elif opcion == 2:
                    productos_lista = self.quick_sort(productos_lista, buscar=por_precio)
                elif opcion == 3:
                    productos_lista = self.quick_sort(productos_lista, buscar=por_stock)
                elif opcion == 4:
                    return
                else:
                    print("Opción inválida... \n")

                print("--- LISTADO DE PRODUCTOS  ---")
                for producto in productos_lista:
                    print(producto)
                self.menu_Salida()
                return


class Buscar():
    def __init__(self, inventario):
        self.Productos = inventario.Productos

    def menu_Salida(self):
        while True:
            opcion = input("\n¿Desea regresar al menú principal o salir? (menu/salir): ").strip().lower()
            if opcion == "menu":
                return
            elif opcion == "salir":
                print("Adiós, vuelva pronto.")
                exit()
            else:
                 print("Opción inválida. Responda 'menu' o 'salir'.")


    def buscar_codigo(self):
            if not self.Productos:
                print("Aún no hay productos en el inventario")
                self.menu.Salida()
                return
            try:
                codigo_buscar = int(input("Ingrese el código del producto: "))
            except ValueError:
                print("Debe ingresar un número válido")
                return
            for producto in self.Productos.values():
                if producto.codigo == codigo_buscar:
                    print("\nProducto encontrado:")
                    print(producto)
                    self.menu_Salida()
                    return

            print("No se encontró ningún producto con ese código.")
            self.menu_Salida()



inventario = Inventario()
listado = Listado(inventario)
busqueda = Buscar(inventario)

while True:
    print("- BIENVENIDO A SMARTSTOCK - ")
    print("----- M E N Ú ----- ")
    print("1. Registro de Producto")
    print("2. Listado de Productos ")
    print("3. Búsqueda de Producto ")
    print("4. Actualizar/Eliminar Producto ")
    print("5. Eliminar Producto ")
    print("6. Salir")

    while True:
        try:
            opcion = int(input("Seleccione una opción:  "))
            if opcion not in range(1, 7):
                print("Opción inválida. Intente nuevamente.  \n")
            else:
                break
        except ValueError:
            print("Debe ingresar un número entero. Intente nuevamente.\n")

    match opcion:
        case 1:
            inventario.agregar()
        case 2:
            listado.ordenamiento()
        case 3:
            busqueda.buscar_codigo()
        case 4:
            codtochange=busqueda.buscar_codigo()
            Inventario.modif(codtochange)
            pass
        case 5:
            codtochange = busqueda.buscar_codigo()
            Inventario.eliminate(codtochange)
            pass
        case 6:
            print("Adiós, vuelva pronto.")
            break
