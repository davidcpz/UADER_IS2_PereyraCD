

class Factorial :
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Factorial, cls).__new__(cls)
        return cls._instance
    
    def calcular(self, n):
        if n < 0:
            raise ValueError("El número debe ser positivo o cero.")
        elif n == 0 or n == 1:
            return 1
        else:
            resultado = 1
            for i in range(2, n + 1):
                resultado *= i
            return resultado    
    
    
    
def main ():
        f1=Factorial()
        f2=Factorial()  

        print("¿Son la misma instancia?", f1 is f2)
        print("Factorial de 5:", f1.calcular(5))

if __name__ == "__main__":
    main()

