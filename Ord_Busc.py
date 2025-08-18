class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre.strip()
        self.categoria = categoria.strip()
        self.precio = float(precio)
        self.stock = stock

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} | {self.categoria} | Precio: {self.precio} | Stock: {self.stock}"


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


    def mostrar(self):
        if not self.Productos:
            print("Aún no hay productos en el inventario.\n")
            while True:
                opcion = input("¿Desea regresar al menú principal? (si/no): ").strip().lower()
                if opcion == "si":
                    return
                elif opcion == "no":
                    print("Adiós, vuelva pronto.")
                    exit()
                else:
                    print("Opción inválida. Responda 'si' o 'no'.")

        while True:
            ver_original = input("¿Desea ver el listado original de productos? (si/no): ").strip().lower()
            productos_lista = list(self.Productos.values())

            if ver_original == "si":
                print("\n--- LISTADO ORIGINAL ---")
                for producto in productos_lista:
                    print(producto)
            elif ver_original != "no":
                print("Opción inválida. Responda 'si' o 'no'.\n")
                continue

            ordenar = input("\n¿Desea ordenar los productos? (si/no): ").strip().lower()
            if ordenar == "no":
                print("Regresando al menú principal...\n")
                return
            elif ordenar != "si":
                print("Opción inválida. Responda 'si' o 'no'.\n")
                continue

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
            else:
                print("Opción inválida. Mostrando sin ordenar.\n")

            print("\n--- LISTADO ORDENADO ---")
            for producto in productos_lista:
                print(producto)

            continuar = input("\n¿Desea ordenar nuevamente? (si/no): ").strip().lower()
            if continuar == "no":
                print("Regresando al menú principal...\n")
                return

inventario = Inventario()
listado = Listado(inventario)

while True:
    print("- BIENVENIDO A SMARTSTOCK - ")
    print("----- M E N Ú ----- ")
    print("1. Registro de Producto")
    print("2. Listado de Productos ")
    print("3. Búsqueda de Producto ")
    print("4. Actualizar/Eliminar Producto ")
    print("5. Salir")

    while True:
        try:
            opcion = int(input("Seleccione una opción:  "))
            if opcion not in range(1, 6):
                print("Opción inválida. Intente nuevamente.  \n")
            else:
                break
        except ValueError:
            print("Debe ingresar un número entero. Intente nuevamente.\n")

    match opcion:
        case 1:
            inventario.agregar()
        case 2:
            listado.mostrar()
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("Adiós, vuelva pronto.")
            break



"""
class Ordenador:
    def listado(self):
        if not  self.Productos:
            print("No hay productos registrados. \n")
            return

        productos_lista = list(self.Productos.values())

        ordenar = input("Desea ordenar los productos? (si/no):  ").strip().lower()
        if ordenar == "no":
            for producto in productos_lista:
                print(producto)
            return
        if ordenar == "si":
            print("Desea ordenar por: ")
            print("1. Nombre")
            print("2. Precio")
            print("3. Stock")

            try:
                opcion = int(input("Seleccione una opcion: "))
            except ValueError:
                print("Debe ingresar un número válido")
"""