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

#class Buscador: