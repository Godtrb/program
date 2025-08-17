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
            precio = float(input("Ingresar año de publicacion del libro: "))
            if(precio <= 0):
                print("Error: No es poscible tener un precio negativo.")
                return
            categoria = input("Ingresar autor del libro: ")
            self.Productos[codigo] = Productos(nombre,categoria,precio,codigo,stuck=True)
            print("Libro agregado.\n")
        except ValueError:
            print("Error: El año de publicacion debe ser un numero entero.\n")
