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