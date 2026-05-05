# TP4 - Punto 2
# Patrón estructural Bridge

from abc import ABC, abstractmethod


class TrenLaminador(ABC):
    """Interfaz del tren laminador."""

    @abstractmethod
    def producir(self) -> str:
        pass


class TrenLaminador5m(TrenLaminador):
    """Implementación concreta: tren de 5 metros."""

    def producir(self) -> str:
        return "Plancha producida en tren laminador de 5 metros."


class TrenLaminador10m(TrenLaminador):
    """Implementación concreta: tren de 10 metros."""

    def producir(self) -> str:
        return "Plancha producida en tren laminador de 10 metros."


class LaminaAcero:
    """Representa una lámina de acero."""

    def __init__(self, tren_laminador: TrenLaminador) -> None:
        self.espesor = '0.5"'
        self.ancho = "1.5 metros"
        self.tren_laminador = tren_laminador

    def producir(self) -> None:
        """Muestra las características de la lámina y el proceso de producción."""
        print("Lámina de acero")
        print(f"Espesor: {self.espesor}")
        print(f"Ancho: {self.ancho}")
        print(self.tren_laminador.producir())


def main() -> None:
    lamina_5m = LaminaAcero(TrenLaminador5m())
    lamina_10m = LaminaAcero(TrenLaminador10m())

    print("Producción con tren de 5 metros:")
    lamina_5m.producir()

    print("\nProducción con tren de 10 metros:")
    lamina_10m.producir()


if __name__ == "__main__":
    main()


