#Primera clase Hija que representa al Platillo
from modelos.producto import Producto
class Platillo(Producto):
    def __init__(self, nombre, precio, disponible, calorias):
        super().__init__(nombre, precio, disponible)
        self.calorias = calorias

    #Se sobreescribe el método
    def mostrar_informacion(self):
        return (
            "Los Platillos son: \n"
            f"{super().mostrar_informacion()}\n"
            f"Calorías: {self.calorias} kcal"
        )
