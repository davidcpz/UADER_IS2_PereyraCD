# Ejercicio 6 - Patrón Prototype

import copy


class Documento:
    """Clase que implementa el patrón Prototype."""

    def __init__(self, titulo, contenido, metadata):
        self.titulo = titulo
        self.contenido = contenido
        self.metadata = metadata

    def clone(self):
        """Devuelve una copia profunda del objeto."""
        return copy.deepcopy(self)

    def mostrar(self):
        return f"Título: {self.titulo}, Metadata: {self.metadata}"


def main():
    # Objeto original
    doc1 = Documento(
        "Informe",
        "Contenido inicial",
        {"version": 1, "autor": "David"}
    )

    print("Original:")
    print(doc1.mostrar())

    # Clon 1
    doc2 = doc1.clone()
    doc2.metadata["version"] = 2

    print("\nClon 1 modificado:")
    print(doc2.mostrar())

    # Clon del clon
    doc3 = doc2.clone()
    doc3.metadata["version"] = 3

    print("\nClon 2 (clon del clon):")
    print(doc3.mostrar())

    print("\nOriginal nuevamente (no debe cambiar):")
    print(doc1.mostrar())


if __name__ == "__main__":
    main()