# TP5 - Punto 5
# Patrón Memento modificado

import os


# =====================
# MEMENTO
# =====================

class Memento:

    def __init__(self, file, content):

        self.file = file
        self.content = content


# =====================
# ORIGINATOR
# =====================

class FileWriterUtility:

    def __init__(self, file):

        self.file = file
        self.content = ""

    def write(self, string):

        self.content += string

    def save(self):

        return Memento(
            self.file,
            self.content
        )

    def undo(self, memento):

        self.file = memento.file
        self.content = memento.content


# =====================
# CARETAKER
# =====================

class FileWriterCaretaker:

    def __init__(self):

        self.historial = []

    def save(self, writer):

        self.historial.append(
            writer.save()
        )

        # Mantiene máximo 4 estados

        if len(self.historial) > 4:
            self.historial.pop(0)

    def undo(self, writer, posicion=0):

        indice = len(self.historial) - 1 - posicion

        if indice >= 0:
            writer.undo(
                self.historial[indice]
            )
        else:
            print(
                "No existe ese estado."
            )


# =====================
# MAIN
# =====================

if __name__ == "__main__":

    os.system("cls")

    caretaker = FileWriterCaretaker()

    writer = FileWriterUtility(
        "archivo.txt"
    )

    writer.write("Estado 1\n")
    caretaker.save(writer)

    writer.write("Estado 2\n")
    caretaker.save(writer)

    writer.write("Estado 3\n")
    caretaker.save(writer)

    writer.write("Estado 4\n")
    caretaker.save(writer)

    writer.write("Estado 5\n")
    caretaker.save(writer)

    print("Contenido actual:")
    print(writer.content)

    print("\nUndo(0):")
    caretaker.undo(writer, 0)
    print(writer.content)

    print("\nUndo(1):")
    caretaker.undo(writer, 1)
    print(writer.content)

    print("\nUndo(2):")
    caretaker.undo(writer, 2)
    print(writer.content)

    print("\nUndo(3):")
    caretaker.undo(writer, 3)
    print(writer.content)