# Abstract Factory

from abc import ABC, abstractmethod


# Productos abstractos

class Mensaje(ABC):
    @abstractmethod
    def contenido(self):
        pass


class Enviador(ABC):
    @abstractmethod
    def enviar(self):
        pass


# Productos concretos EMAIL

class MensajeEmail(Mensaje):
    def contenido(self):
        return "Mensaje enviado por Email"


class EnviadorEmail(Enviador):
    def enviar(self):
        return "Enviando Email..."


# Productos concretos SMS

class MensajeSMS(Mensaje):
    def contenido(self):
        return "Mensaje enviado por SMS"


class EnviadorSMS(Enviador):
    def enviar(self):
        return "Enviando SMS..."


# Abstract Factory

class FabricaNotificacion(ABC):
    @abstractmethod
    def crear_mensaje(self):
        pass

    @abstractmethod
    def crear_enviador(self):
        pass


# Fábricas concretas

class FabricaEmail(FabricaNotificacion):
    def crear_mensaje(self):
        return MensajeEmail()

    def crear_enviador(self):
        return EnviadorEmail()


class FabricaSMS(FabricaNotificacion):
    def crear_mensaje(self):
        return MensajeSMS()

    def crear_enviador(self):
        return EnviadorSMS()


# Cliente

class Aplicacion:
    def __init__(self, fabrica):
        self.mensaje = fabrica.crear_mensaje()
        self.enviador = fabrica.crear_enviador()

    def ejecutar(self):
        print(self.mensaje.contenido())
        print(self.enviador.enviar())


def main():
    print("=== Email ===")
    app_email = Aplicacion(FabricaEmail())
    app_email.ejecutar()

    print("\n=== SMS ===")
    app_sms = Aplicacion(FabricaSMS())
    app_sms.ejecutar()


if __name__ == "__main__":
    main()