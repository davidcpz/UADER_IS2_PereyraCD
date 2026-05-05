
# TP4 - Punto 3
# Patrón estructural Composite

from abc import ABC, abstractmethod


class Componente(ABC):
    """Interfaz común para piezas simples y conjuntos compuestos."""

    @abstractmethod
    def mostrar(self, nivel: int = 0) -> None:
        pass


class Pieza(Componente):
    """Representa una pieza individual."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def mostrar(self, nivel: int = 0) -> None:
        indentacion = "  " * nivel
        print(f"{indentacion}- Pieza: {self.nombre}")


class Conjunto(Componente):
    """Representa un conjunto que puede contener piezas u otros conjuntos."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente: Componente) -> None:
        self.componentes.append(componente)

    def mostrar(self, nivel: int = 0) -> None:
        indentacion = "  " * nivel
        print(f"{indentacion}+ Conjunto: {self.nombre}")

        for componente in self.componentes:
            componente.mostrar(nivel + 1)


def crear_subconjunto(nombre: str) -> Conjunto:
    """Crea un subconjunto con cuatro piezas."""
    subconjunto = Conjunto(nombre)

    for i in range(1, 5):
        subconjunto.agregar(Pieza(f"Pieza {i}"))

    return subconjunto


def main() -> None:
    producto_principal = Conjunto("Producto principal")

    producto_principal.agregar(crear_subconjunto("Subconjunto 1"))
    producto_principal.agregar(crear_subconjunto("Subconjunto 2"))
    producto_principal.agregar(crear_subconjunto("Subconjunto 3"))

    print("Estructura inicial del producto:")
    producto_principal.mostrar()

    print("\nAgregando subconjunto opcional...\n")

    producto_principal.agregar(crear_subconjunto("Subconjunto opcional"))

    print("Estructura final del producto:")
    producto_principal.mostrar()


if __name__ == "__main__":
    main()