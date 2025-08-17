class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("El código debe ser un número entero positivo.")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede quedar vacío.")
        if not isinstance(categoria, str) or not categoria.strip():
            raise ValueError("La categoría no puede quedar vacía.")
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser un número positivo.")
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("El stock debe ser un número entero no negativo.")

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
            try:
                codigo = int(input("Ingrese código del producto (entero positivo): "))
                if codigo in self.Productos:
                    print("Error: El código ya existe en el inventario.\n")
                    continue

                nombre = input("Ingrese nombre: ")
                categoria = input("Ingrese categoría: ")
                precio = float(input("Ingrese precio: "))
                stock = int(input("Ingrese stock: "))

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

            except ValueError as ve:
                print("Intente de nuevo.\n")