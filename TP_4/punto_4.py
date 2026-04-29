# Ejercicio 4 - Patrón Factory

from abc import ABC, abstractmethod


class Factura(ABC):
    """Clase base abstracta para facturas."""

    def __init__(self, importe: float) -> None:
        self.importe = importe

    @abstractmethod
    def mostrar(self) -> str:
        pass


class FacturaIVAResponsable(Factura):
    """Factura para cliente IVA Responsable."""

    def mostrar(self) -> str:
        return f"Factura IVA Responsable - Importe total: ${self.importe}"


class FacturaIVANoInscripto(Factura):
    """Factura para cliente IVA No Inscripto."""

    def mostrar(self) -> str:
        return f"Factura IVA No Inscripto - Importe total: ${self.importe}"


class FacturaIVAExento(Factura):
    """Factura para cliente IVA Exento."""

    def mostrar(self) -> str:
        return f"Factura IVA Exento - Importe total: ${self.importe}"


class FacturaFactory:
    """Fábrica encargada de crear facturas según condición impositiva."""

    @staticmethod
    def crear_factura(condicion: str, importe: float) -> Factura:
        condicion_normalizada = condicion.strip().lower()

        if condicion_normalizada == "responsable":
            return FacturaIVAResponsable(importe)
        if condicion_normalizada == "no_inscripto":
            return FacturaIVANoInscripto(importe)
        if condicion_normalizada == "exento":
            return FacturaIVAExento(importe)

        raise ValueError(
            f"Condición impositiva no soportada: '{condicion}'. "
            "Opciones válidas: responsable, no_inscripto, exento."
        )


def main() -> None:
    casos = [
        ("responsable", 1000),
        ("no_inscripto", 1500),
        ("exento", 2000),
        ("monotributo", 1200),
    ]

    for condicion, importe in casos:
        try:
            factura = FacturaFactory.crear_factura(condicion, importe)
            print(factura.mostrar())
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()