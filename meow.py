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
            self.Productos[codigo] = Productos(nombre,categoria,precio,codigo,stock)
            print("producto agregado.\n")
        except ValueError:
            print("Error: El precio del producto debe ser un numero entero.\n")

def modif(