

class Impuesto:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Impuesto, cls).__new__(cls)
        return cls._instance
    
    def calcular_iva(self, monto):
        return monto * 0.21  # Ejemplo de cálculo de impuesto

    def calcular_iibb(self, monto):
        return monto * 0.05  # Ejemplo de cálculo de ingresos brutos

    def calcular_municipal(self, monto):
        return monto * 0.012  # Ejemplo de cálculo de impuesto municipal   

def main():
    impuesto1 = Impuesto()
    impuesto2 = Impuesto()

    print("¿Son la misma instancia?", impuesto1 is impuesto2)
    imp=Impuesto()
    print ("IVA 21% de 1000:", imp.calcular_iva(1000))
    print ("IIBB 5% de 1000:", imp.calcular_iibb(1000))
    print ("Municipal 1.2% de 1000:", imp.calcular_municipal(1000))

if __name__ == "__main__":
    main()

    