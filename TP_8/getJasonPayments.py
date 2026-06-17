"""
TP8 - Ingeniería Reversa, Re-factoría y Re-Ingeniería.

Sistema de pagos automatizado que selecciona una cuenta bancaria
según disponibilidad de saldo y balanceo de pagos.

Versión: 1.2
"""

VERSION = "1.2"

SALDO_TOKEN1 = 1000
SALDO_TOKEN2 = 2000
MONTO_PAGO = 500
CANTIDAD_PEDIDOS = 7
import json
from pathlib import Path

class JsonTokenManager:
    """Gestiona la lectura de tokens desde un archivo JSON usando Singleton."""

    _instance = None

    def __new__(cls, json_file="sitedata.json"):
        """Crea una única instancia de la clase."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.json_file = Path(json_file)
            cls._instance.tokens = cls._instance._load_tokens()
        return cls._instance

    def _load_tokens(self):
        """Carga los tokens desde el archivo JSON."""
        with open(self.json_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_token(self, token_name):
        """Devuelve la clave asociada a un token."""
        return self.tokens[token_name]

class Cuenta:
    """Representa una cuenta bancaria."""

    def __init__(self, token, saldo):
        self.token = token
        self.saldo = saldo

    def tiene_saldo(self, monto):
        """Verifica si la cuenta tiene saldo suficiente."""
        return self.saldo >= monto

    def pagar(self, monto):
        """Descuenta el monto del saldo."""
        self.saldo -= monto


class Pago:
    """Representa una solicitud de pago."""

    def __init__(self, numero_pedido, monto):
        self.numero_pedido = numero_pedido
        self.monto = monto
        self.token_utilizado = None
        self.clave_utilizada = None


class ManejadorCuenta:
    """Manejador base para la cadena de responsabilidad."""

    def __init__(self, cuenta):
        self.cuenta = cuenta
        self.siguiente = None

    def set_siguiente(self, siguiente):
        """Define el siguiente elemento de la cadena."""
        self.siguiente = siguiente

    def procesar_pago(self, pago):
        """Procesa un pago o lo deriva al siguiente manejador."""

        if self.cuenta.tiene_saldo(pago.monto):
            self.cuenta.pagar(pago.monto)
            pago.token_utilizado = self.cuenta.token
            pago.clave_utilizada = JsonTokenManager().get_token(self.cuenta.token)
            
            print(
                f"Pedido {pago.numero_pedido} "
                f"pagado con {self.cuenta.token} "
                f"por ${pago.monto}"
                f" (clave: {pago.clave_utilizada})"
            )

            return True

        if self.siguiente:
            return self.siguiente.procesar_pago(pago)

        print(
            f"Pedido {pago.numero_pedido} "
            f"rechazado: saldo insuficiente."
        )

        return False
    
class ControladorPagos:
    """Controla el ruteo alternado de pagos."""

    def __init__(self, handler1, handler2):
        self.historial = HistorialPagos()
        self.handler1 = handler1
        self.handler2 = handler2
        self.turno = 0

    def procesar(self, pago):
        """Procesa un pago alternando las cuentas."""

        if self.turno % 2 == 0:
            resultado = self.handler1.procesar_pago(pago)
        else:
            resultado = self.handler2.procesar_pago(pago)

        if resultado:
            self.historial.agregar(pago)

        self.turno += 1
        return resultado



class PagoIterator:
    """Iterador para recorrer pagos en orden cronológico."""

    def __init__(self, pagos):
        self.pagos = pagos
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice >= len(self.pagos):
            raise StopIteration

        pago = self.pagos[self.indice]
        self.indice += 1
        return pago


class HistorialPagos:
    """Colección de pagos realizados."""

    def __init__(self):
        self.pagos = []

    def agregar(self, pago):
        """Agrega un pago al historial."""
        self.pagos.append(pago)

    def __iter__(self):
        return PagoIterator(self.pagos)


def main():
    """Ejecuta una prueba completa del sistema de pagos."""

    cuenta1 = Cuenta("token1", SALDO_TOKEN1)
    cuenta2 = Cuenta("token2", SALDO_TOKEN2)

    handler1 = ManejadorCuenta(cuenta1)
    handler2 = ManejadorCuenta(cuenta2)

    handler1.set_siguiente(handler2)
    handler2.set_siguiente(None)

    controlador = ControladorPagos(handler1, handler2)

    for numero in range(1, CANTIDAD_PEDIDOS + 1):
        pago = Pago(numero, MONTO_PAGO)
        controlador.procesar(pago)

    print()
    print("Listado cronológico de pagos")


    for pago in controlador.historial:
        print(
            f"Pedido {pago.numero_pedido} - "
            f"${pago.monto} - "
            f"{pago.token_utilizado} - "
            f"Clave: {pago.clave_utilizada}"
        )

    print()
    print("Saldos finales")
    print("token1:", cuenta1.saldo)
    print("token2:", cuenta2.saldo)


if __name__ == "__main__":
    main()
    