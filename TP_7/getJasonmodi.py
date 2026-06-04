"""
TP7 - Ingeniería Reversa, Refactoría y Reingeniería

Programa reutilizable para recuperar claves almacenadas
en un archivo JSON.

Implementa Programación Orientada a Objetos y patrón Singleton.

Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.
"""

import json
import sys


class JsonTokenManager:
    """
    Clase Singleton responsable de leer un archivo JSON
    y recuperar el valor asociado a una clave determinada.
    """

    _instance = None

    def __new__(cls):
        """Garantiza que exista una única instancia de la clase."""
        if cls._instance is None:
            cls._instance = super(JsonTokenManager, cls).__new__(cls)
        return cls._instance

    def obtener_clave(self, jsonfile, jsonkey="token1"):
        """Recupera el valor de una clave existente en un archivo JSON."""
        with open(jsonfile, "r", encoding="utf-8") as myfile:
            data = json.load(myfile)

        if jsonkey not in data:
            raise KeyError(f"La clave '{jsonkey}' no existe en el archivo JSON.")

        return data[jsonkey]


def main():
    """Punto de entrada del programa."""
    if len(sys.argv) < 2:
        print("Uso: python getJasonmodi.py archivo.json [clave]")
        return

    jsonfile = sys.argv[1]

    if len(sys.argv) >= 3:
        jsonkey = sys.argv[2]
    else:
        jsonkey = "token1"

    manager = JsonTokenManager()

    try:
        print(manager.obtener_clave(jsonfile, jsonkey))
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{jsonfile}'.")
    except KeyError as error:
        print(f"Error: {error}")
    except json.JSONDecodeError:
        print("Error: el archivo no contiene un JSON válido.")


if __name__ == "__main__":
    main()