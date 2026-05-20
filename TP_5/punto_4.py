# TP5 - Punto 4
# Patrón State modificado

import os


class State:

    def scan(self):

        self.pos += 1

        if self.pos == len(self.stations):
            self.pos = 0

        print(
            f"Sintonizando... Estación "
            f"{self.stations[self.pos]} {self.name}"
        )

        self.radio.scan_memorias()


# =======================
# AM
# =======================

class AmState(State):

    def __init__(self, radio):

        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):

        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate


# =======================
# FM
# =======================

class FmState(State):

    def __init__(self, radio):

        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):

        print("Cambiando a AM")
        self.radio.state = self.radio.amstate


# =======================
# RADIO
# =======================

class Radio:

    def __init__(self):

        self.fmstate = FmState(self)
        self.amstate = AmState(self)

        self.state = self.fmstate

        self.memorias = {
            "M1": ("FM", "95.5"),
            "M2": ("AM", "1450"),
            "M3": ("FM", "101.7"),
            "M4": ("AM", "1600")
        }

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

    def scan_memorias(self):

        print("Memorias:")

        for memoria, datos in self.memorias.items():

            banda, frecuencia = datos

            print(
                f"{memoria}: "
                f"{banda} {frecuencia}"
            )


# =======================

if __name__ == "__main__":

    os.system("cls")

    radio = Radio()

    acciones = (
        [radio.scan] * 3
        + [radio.toggle_amfm]
        + [radio.scan] * 3
    )

    acciones *= 2

    for accion in acciones:
        accion()