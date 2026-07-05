#Se crea la clase que será Padre con el nombre Producto
class Producto:
    def __init__(self, nombre, precio, disponible):
        self.nombre = nombre
        self.__precio = precio  #Se realiza la encapsulación
        self.disponible = disponible
    
    #Se crean los métodos getters y setters
    #El método de acceso
    def obtener_precio(self):
        return self.__precio

    #El método de modificación
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor a 0")

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return (
            f"Nombre: {self.nombre}\n"
            f"Precio: ${self.__precio:.2f}\n"
            f"Estado: {estado}"
        )
