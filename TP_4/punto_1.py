# TP4 - Punto 1
# Patrón estructural Proxy

import os


class Ping:
    """Clase real que ejecuta el ping."""

    def execute(self, direccion: str) -> None:
        """
        Ejecuta ping solo si la dirección comienza con 192.
        """
        if direccion.startswith("192."):
            print(f"Ejecutando ping controlado a {direccion}")
            os.system(f"ping -n 10 {direccion}")
        else:
            print("Dirección no permitida. Debe comenzar con 192.")

    def executefree(self, direccion: str) -> None:
        """
        Ejecuta ping sin validar la dirección.
        """
        print(f"Ejecutando ping libre a {direccion}")
        os.system(f"ping -n 10 {direccion}")


class PingProxy:
    """Proxy que controla el acceso a la clase Ping."""

    def __init__(self) -> None:
        self.ping = Ping()

    def execute(self, direccion: str) -> None:
        """
        Si la dirección es 192.168.0.254, redirige a www.google.com.
        En caso contrario, delega la ejecución en Ping.
        """
        if direccion == "192.168.0.254":
            print("Proxy detectó dirección especial.")
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(direccion)


def main() -> None:
    proxy = PingProxy()

    print("Caso 1: IP permitida")
    proxy.execute("192.168.0.10")

    print("\nCaso 2: IP especial redirigida")
    proxy.execute("192.168.0.254")

    print("\nCaso 3: IP no permitida")
    proxy.execute("10.0.0.1")


if __name__ == "__main__":
    main()