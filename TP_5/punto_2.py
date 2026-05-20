# TP5 - Punto 2
# Patrón Iterator


class IteradorDirecto:
    """Recorre la cadena de izquierda a derecha."""

    def __init__(self, cadena):
        self.cadena = cadena
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.indice >= len(self.cadena):
            raise StopIteration

        caracter = self.cadena[self.indice]
        self.indice += 1

        return caracter


class IteradorReverso:
    """Recorre la cadena de derecha a izquierda."""

    def __init__(self, cadena):
        self.cadena = cadena
        self.indice = len(cadena) - 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.indice < 0:
            raise StopIteration

        caracter = self.cadena[self.indice]
        self.indice -= 1

        return caracter


class Cadena:
    """Colección que almacena una cadena."""

    def __init__(self, texto):
        self.texto = texto

    def directo(self):
        return IteradorDirecto(self.texto)

    def reverso(self):
        return IteradorReverso(self.texto)


def main():

    texto = Cadena("ingenieria de software")

    print("Recorrido directo:")

    for letra in texto.directo():
        print(letra, end=" ")

    print("\n")

    print("Recorrido reverso:")

    for letra in texto.reverso():
        print(letra, end=" ")


if __name__ == "__main__":
    main()