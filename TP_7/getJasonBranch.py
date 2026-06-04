"""
TP7 - Ingeniería Reversa, Refactoría y Reingeniería

Programa reutilizable para recuperar claves almacenadas
en un archivo JSON.

Implementa:
- Programación Orientada a Objetos
- Singleton
- Branching by Abstraction

Copyright UADER-FCyT-IS2©2024
Todos los derechos reservados.
"""

import json
import sys
from abc import ABC, abstractmethod
VERSION= "1.1"

class TokenProvider(ABC):
    """
    Abstracción utilizada para aplicar
    Branching by Abstraction.
    """

    @abstractmethod
    def obtener_clave(self, jsonfile, jsonkey):
        """Obtiene una clave desde un origen de datos."""
        pass


class JsonTokenManager(TokenProvider):
    """
    Implementación concreta encargada
    de recuperar claves desde archivos JSON.
    """

    _instance = None

    def __new__(cls):
        """
        Implementación del patrón Singleton.
        """
        if cls._instance is None:
            cls._instance = super(JsonTokenManager, cls).__new__(cls)

        return cls._instance

    def obtener_clave(self, jsonfile, jsonkey="token1"):
        """
        Recupera una clave desde un archivo JSON.
        """

        with open(jsonfile, "r", encoding="utf-8") as myfile:
            data = json.load(myfile)

        if jsonkey not in data:
            raise KeyError(
                f"La clave '{jsonkey}' no existe en el archivo JSON."
            )

        return data[jsonkey]


def main():
    """
    Punto de entrada del programa.
    """

    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        print(f"Versión {VERSION}")
        return

    if len(sys.argv) < 2:
        print(
            "Uso: python getJasonBranch.py archivo.json [clave]"
        )
        return

    jsonfile = sys.argv[1]

    if len(sys.argv) >= 3:
        jsonkey = sys.argv[2]
    else:
        jsonkey = "token1"

    manager = JsonTokenManager()

    try:
        print(
            manager.obtener_clave(
                jsonfile,
                jsonkey
            )
        )

    except FileNotFoundError:
        print(
            f"Error: no se encontró el archivo '{jsonfile}'."
        )

    except KeyError as error:
        print(
            f"Error: {error}"
        )

    except json.JSONDecodeError:
        print(
            "Error: el archivo no contiene un JSON válido."
        )


if __name__ == "__main__":
    main()