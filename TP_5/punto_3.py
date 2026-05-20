# TP5 - Punto 3
# Patrón Observer

from abc import ABC, abstractmethod


# ==========================
# OBSERVER
# ==========================

class Observador(ABC):

    @abstractmethod
    def actualizar(self, id_emitido):
        pass


# ==========================
# OBSERVADORES CONCRETOS
# ==========================

class ClienteID(Observador):

    def __init__(self, mi_id):
        self.mi_id = mi_id

    def actualizar(self, id_emitido):

        if self.mi_id == id_emitido:
            print(f"ID {self.mi_id}: Coincidencia encontrada")


# ==========================
# SUBJECT
# ==========================

class Emisor:

    def __init__(self):
        self.observadores = []

    def suscribir(self, observador):
        self.observadores.append(observador)

    def emitir(self, id_emitido):

        print(f"\nEmitiendo ID: {id_emitido}")

        for observador in self.observadores:
            observador.actualizar(id_emitido)


# ==========================
# MAIN
# ==========================

def main():

    emisor = Emisor()

    obs1 = ClienteID("AB12")
    obs2 = ClienteID("CD34")
    obs3 = ClienteID("EF56")
    obs4 = ClienteID("GH78")

    emisor.suscribir(obs1)
    emisor.suscribir(obs2)
    emisor.suscribir(obs3)
    emisor.suscribir(obs4)

    ids = [
        "AB12",
        "XX99",
        "CD34",
        "ZZ11",
        "EF56",
        "AA22",
        "GH78",
        "QQ55"
    ]

    for id_actual in ids:
        emisor.emitir(id_actual)


if __name__ == "__main__":
    main()