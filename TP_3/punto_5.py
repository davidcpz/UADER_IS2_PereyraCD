# Ejercicio 5 - Patrón Builder
# Construcción de aviones

from abc import ABC, abstractmethod


class Avion:
    """Producto complejo que se construye paso a paso."""

    def __init__(self) -> None:
        self.partes = []

    def agregar(self, parte: str) -> None:
        self.partes.append(parte)

    def mostrar(self) -> str:
        return "Avión construido con:\n  - " + "\n  - ".join(self.partes)


class BuilderAvion(ABC):
    """Interfaz abstracta del Builder de aviones."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._producto = Avion()

    def obtener_resultado(self) -> Avion:
        avion = self._producto
        self.reset()
        return avion

    @abstractmethod
    def construir_body(self) -> None:
        pass

    @abstractmethod
    def construir_turbinas(self) -> None:
        pass

    @abstractmethod
    def construir_alas(self) -> None:
        pass

    @abstractmethod
    def construir_tren_aterrizaje(self) -> None:
        pass


class BuilderAvionComercial(BuilderAvion):
    """Builder concreto para construir un avión comercial."""

    def construir_body(self) -> None:
        self._producto.agregar("Body de avión comercial")

    def construir_turbinas(self) -> None:
        self._producto.agregar("2 turbinas comerciales")

    def construir_alas(self) -> None:
        self._producto.agregar("2 alas principales")

    def construir_tren_aterrizaje(self) -> None:
        self._producto.agregar("Tren de aterrizaje")


class Director:
    """Define el orden de construcción del avión."""

    def __init__(self, builder: BuilderAvion) -> None:
        self._builder = builder

    def construir_avion_completo(self) -> None:
        self._builder.construir_body()
        self._builder.construir_turbinas()
        self._builder.construir_alas()
        self._builder.construir_tren_aterrizaje()


def main() -> None:
    builder = BuilderAvionComercial()
    director = Director(builder)

    director.construir_avion_completo()
    avion = builder.obtener_resultado()

    print(avion.mostrar())


if __name__ == "__main__":
    main()