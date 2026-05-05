# TP4 - Punto 4
# Patrón estructural Decorator

from abc import ABC, abstractmethod


# =========================
# COMPONENTE
# =========================

class Componente(ABC):
    @abstractmethod
    def operar(self) -> float:
        pass


class Numero(Componente):
    """Número base"""

    def __init__(self, valor: float) -> None:
        self.valor = valor

    def operar(self) -> float:
        return self.valor


# =========================
# DECORADOR BASE
# =========================

class Decorador(Componente):
    def __init__(self, componente: Componente) -> None:
        self._componente = componente

    @abstractmethod
    def operar(self) -> float:
        pass


# =========================
# DECORADORES CONCRETOS
# =========================

class Sumar2(Decorador):
    def operar(self) -> float:
        return self._componente.operar() + 2


class Multiplicar2(Decorador):
    def operar(self) -> float:
        return self._componente.operar() * 2


class Dividir3(Decorador):
    def operar(self) -> float:
        return self._componente.operar() / 3


# =========================
# MAIN
# =========================

def main() -> None:
    numero = Numero(5)

    print("Número original:")
    print(numero.operar())

    # Decoración anidada
    numero_decorado = Dividir3(Multiplicar2(Sumar2(numero)))

    print("\nNúmero con decoradores ( +2, *2, /3 ):")
    print(numero_decorado.operar())

    print("\nValidación paso a paso:")
    print("5 + 2 =", Sumar2(numero).operar())
    print("(5 + 2) * 2 =", Multiplicar2(Sumar2(numero)).operar())
    print("((5 + 2) * 2) / 3 =", Dividir3(Multiplicar2(Sumar2(numero))).operar())


if __name__ == "__main__":
    main()