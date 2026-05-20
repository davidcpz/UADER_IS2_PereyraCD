# TP5 - Punto 1
# Patrón de comportamiento: Chain of Responsibility


class Manejador:
    """Clase base para los manejadores de la cadena."""

    def __init__(self):
        self.siguiente = None

    def establecer_siguiente(self, manejador):
        self.siguiente = manejador
        return manejador

    def manejar(self, numero):
        if self.siguiente:
            return self.siguiente.manejar(numero)

        print(f"{numero}: no consumido")
        return None


class ManejadorPrimos(Manejador):
    """Consume números primos."""

    def es_primo(self, numero):
        if numero < 2:
            return False

        for divisor in range(2, int(numero**0.5) + 1):
            if numero % divisor == 0:
                return False

        return True

    def manejar(self, numero):
        if self.es_primo(numero):
            print(f"{numero}: consumido por ManejadorPrimos")
            return True

        return super().manejar(numero)


class ManejadorPares(Manejador):
    """Consume números pares."""

    def manejar(self, numero):
        if numero % 2 == 0:
            print(f"{numero}: consumido por ManejadorPares")
            return True

        return super().manejar(numero)


def main():
    manejador_primos = ManejadorPrimos()
    manejador_pares = ManejadorPares()

    manejador_primos.establecer_siguiente(manejador_pares)

    for numero in range(1, 101):
        manejador_primos.manejar(numero)


if __name__ == "__main__":
    main()