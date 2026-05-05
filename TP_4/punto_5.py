# TP4 - Punto 5
# Patrón Flyweight

class Arbol:
    """Flyweight: comparte datos comunes"""
    
    def __init__(self, tipo, color, textura):
        self.tipo = tipo
        self.color = color
        self.textura = textura

    def mostrar(self, x, y):
        print(f"Árbol {self.tipo} en ({x},{y}) color {self.color}")


class FabricaArboles:
    """Fábrica de Flyweights"""

    _arboles = {}

    @classmethod
    def obtener_arbol(cls, tipo, color, textura):
        clave = (tipo, color, textura)

        if clave not in cls._arboles:
            cls._arboles[clave] = Arbol(tipo, color, textura)

        return cls._arboles[clave]


def main():
    arbol1 = FabricaArboles.obtener_arbol("Pino", "Verde", "Textura1")
    arbol2 = FabricaArboles.obtener_arbol("Pino", "Verde", "Textura1")

    arbol1.mostrar(10, 20)
    arbol2.mostrar(50, 60)

    print("\n¿Son el mismo objeto?", arbol1 is arbol2)


if __name__ == "__main__":
    main()