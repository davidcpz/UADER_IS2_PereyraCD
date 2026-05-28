"""
TP6 - Ingeniería Reversa y Reingeniería

Programa reutilizable para recuperar claves almacenadas
en un archivo JSON.

Permite:
- recuperar token1 por defecto
- recuperar cualquier clave indicada por argumento
- validar errores de archivo y claves inexistentes
"""

import json
import sys


def obtener_clave(jsonfile, jsonkey="token1"):
    """Recupera el valor de una clave existente en un archivo JSON."""
    with open(jsonfile, "r", encoding="utf-8") as myfile:
        data = json.load(myfile)

    if jsonkey not in data:
        raise KeyError(f"La clave '{jsonkey}' no existe en el archivo JSON.")

    return data[jsonkey]


def main():
    if len(sys.argv) < 2:
        print("Uso: python getJason.py archivo.json [clave]")
        return

    jsonfile = sys.argv[1]

    if len(sys.argv) >= 3:
        jsonkey = sys.argv[2]
    else:
        jsonkey = "token1"

    try:
        print(obtener_clave(jsonfile, jsonkey))
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{jsonfile}'.")
    except KeyError as error:
        print(f"Error: {error}")
    except json.JSONDecodeError:
        print("Error: el archivo no contiene un JSON válido.")


if __name__ == "__main__":
    main()