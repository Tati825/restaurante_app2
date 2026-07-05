from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def main():

    #Se crea el reataurante
    restaurante = Restaurante()

    #Se crean 2 platillos de ejemplo
    platillo1 = Platillo(
        "Salchipapa",
        2.50,
        True,
        600
    )

    platillo2 = Platillo(
        "Bandejita",
        4.00,
        True,
        900
    )

    #Se crean 2 bebidas de ejemplo
    bebida1 = Bebida(
        "Coca-Cola",
        1.75,
        True,
        500
    )

    bebida2 = Bebida(
        "Yogurt 1 lt",
        3.00,
        False,
        1000
    )

    #Se modifica el precio de la primera bebida
    bebida1.cambiar_precio(2.00)

    #Se intenta colocar un precio no válido para ver el msj de error
    bebida2.cambiar_precio(-1)

    #Se agregan los productos creados al restaurante
    restaurante.agregar_producto(platillo1)
    restaurante.agregar_producto(platillo2)
    restaurante.agregar_producto(bebida1)
    restaurante.agregar_producto(bebida2)

    #Se muestran todos los productos
    restaurante.mostrar_productos()


if __name__ == "__main__":
    main()
