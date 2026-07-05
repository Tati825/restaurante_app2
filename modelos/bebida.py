#Segunda clase hija que representa a las Bebidas
from modelos.producto import Producto
class Bebida(Producto):
    def __init__(self, nombre, precio, disponible, volumen_ml):
        super().__init__(nombre, precio, disponible)
        self.volumen_ml = volumen_ml

    #Se sobreescribe el método
    def mostrar_informacion(self):
        return (
            "Las bebidas son: \n"
            f"{super().mostrar_informacion()}\n"
            f"Volumen: {self.volumen_ml} ml"
        )
