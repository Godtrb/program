### PROYECTO 
- Programación Orientada a Objetos (POO)
- Se aplica el Principio de Responsabilidad Única (SRP) de SOLID. 
- Cuida la experiencia de usuario (UX) en consola.
- Implementa Quick Sort para listas de productos.
- Implementa búsqueda secuencial.



**TABLA DE CONTENIDOS**

[TOCM]

[TOC]
#Godtrb

####Código
**Ingreso de datos y sus validaciones**
Se puede observar que el código no se puede repetir y acepta únicamente números enteros positivos
```html
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

```
**Elimina**
El método pop() elimina el elemento con la clave especificada y devuelve su último valor.
```html
 def modif(self, codigo):
        self.Productos[codigo].pop()
        print("Producto eliminado correctamente.")

```





----
                    

#Jalegosa

####Código
** Ordenamiento Quick Sort**
Este ordenamiento recursivo nos permite realizar el ordenamiento en base a la solicitud del usuario, en este caso  la función buscar nos sirve para comparar elementos y determinar su posición relativa con respecto al pivote
```html
def quick_sort(self, lista, buscar):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if buscar(x) < buscar(pivote)]
        iguales = [x for x in lista if buscar(x) == buscar(pivote)]
        mayores = [x for x in lista[1:] if buscar(x) > buscar(pivote)]
        return self.quick_sort(menores, buscar) + iguales + self.quick_sort(mayores, buscar)
```
**Búsqueda por código**
Verificación de datos dentro de Productos y devuelve los valores sí en dado caso hay coincidencia con el código caso contrario pregunta si desea salir o regresar al menú principal
```html
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
```





----
                    

###Fin
