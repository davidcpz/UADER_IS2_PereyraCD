
from abc import ABC, abstractmethod


class EntregaHamburguesa(ABC):
    """Clase base abstracta para los métodos de entrega de una hamburguesa."""

    @abstractmethod
    def entregar(self) -> str:
        pass


class EntregaMostrador(EntregaHamburguesa):
    """Entrega de hamburguesa por mostrador."""

    def entregar(self) -> str:
        return "La hamburguesa se entrega en mostrador."


class EntregaRetiroCliente(EntregaHamburguesa):
    """Entrega de hamburguesa retirada por el cliente."""

    def entregar(self) -> str:
        return "La hamburguesa será retirada por el cliente."


class EntregaDelivery(EntregaHamburguesa):
    """Entrega de hamburguesa por delivery."""

    def entregar(self) -> str:
        return "La hamburguesa será enviada por delivery."


class HamburguesaFactory:
    """Fábrica encargada de crear el método de entrega de la hamburguesa."""

    @staticmethod
    def crear_entrega(tipo: str) -> EntregaHamburguesa:
        tipo_normalizado = tipo.strip().lower()

        if tipo_normalizado == "mostrador":
            return EntregaMostrador()
        if tipo_normalizado == "retiro":
            return EntregaRetiroCliente()
        if tipo_normalizado == "delivery":
            return EntregaDelivery()

        raise ValueError(
            f"Tipo de entrega no soportado: '{tipo}'. "
            "Opciones válidas: mostrador, retiro, delivery."
        )


def main() -> None:
    tipos_entrega = ["mostrador", "retiro", "delivery", "correo"]

    for tipo in tipos_entrega:
        try:
            entrega = HamburguesaFactory.crear_entrega(tipo)
            print(f"{tipo!r} -> {entrega.entregar()}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()