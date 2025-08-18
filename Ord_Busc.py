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
                        print("Error: El precio debe ser un número positivo.\n")
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


inventario = Inventario()

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
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("Adiós, vuelva pronto.")
            break