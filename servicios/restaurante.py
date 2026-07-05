#Clase para administrar los productos en el Restaurante
class Restaurante:
    def __init__(self):
        self.productos = []

    #Se agrega un producto a la lista
    def agregar_producto(self, producto):
        self.productos.append(producto)

    #Se muestran todos los productos que estén registrados
    def mostrar_productos(self):
        print("\n Menú \n")
        for producto in self.productos:  #Polimorfismo
            print(producto.mostrar_informacion())
