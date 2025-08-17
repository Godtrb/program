class Productos:
    def __init__(self, nombre, categoria, precio,codigo,stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria= categoria
        self.precio= precio
        self.stock = stock
class Inventario:
    def __init__(self):
        self.Productos = {}

    def agregar(self):
        try:
            codigo = input("Ingresar codigo del producto: ")
            if codigo in self.Productos:
                print("Ya existe un producto bajo este codigo.\n")
                return

            nombre = input("Ingresar nombre del producto: ")
            precio = float(input("Ingresar precio del producto: "))
            if(precio <= 0):
                print("Error: No es posible tener un precio negativo.")
                return
            categoria = input("Ingresar categoria del producto: ")
            stock= int(input("Ingresar numero del producto en existencia: "))
            if stock <=0:
                print("Error: No es posible tener un stock negativo.")
                return
            self.Productos[codigo] = Productos(nombre,categoria,precio,codigo,stock)
            print("producto agregado.\n")
        except ValueError:
            print("Error: El precio del producto debe ser un numero.\n")

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
                print("Opción iválida. Intente nuevamente.  \n")
            else:
                break
        except ValueError:
            print("Debe ingresar un número entero. Intente nuevamente.\n")

    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            print("Adiós, vuelva pronto.")
            break
