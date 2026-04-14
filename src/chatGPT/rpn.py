import math

# MEMORIAS (00–09)
memoria = {f"{i:02}": 0 for i in range(10)}

# EXCEPCIÓN PERSONALIZADA

class RPNError(Exception):
    pass

# FUNCIÓN PRINCIPAL DE EVALUACIÓN RPN

def evaluar_rpn(expresion):
    stack = []
    tokens = expresion.split()

    for token in tokens:

        
        # COMANDOS DE PILA
        
        if token == "dup":
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para dup")
            stack.append(stack[-1])

        elif token == "swap":
            if len(stack) < 2:
                raise RPNError("Pila insuficiente para swap")
            stack[-1], stack[-2] = stack[-2], stack[-1]

        elif token == "drop":
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para drop")
            stack.pop()

        elif token == "clear":
            stack.clear()

        
        # CONSTANTES MATEMÁTICAS
        
        elif token == "p":  # π
            stack.append(math.pi)

        elif token == "e":  # e
            stack.append(math.e)

        elif token == "j":  # φ
            stack.append((1 + 5 ** 0.5) / 2)

        
        # FUNCIONES MATEMÁTICAS 
        
        elif token == "sqrt":
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para sqrt")
            x = stack.pop()
            if x < 0:
                raise RPNError("No se puede calcular sqrt de número negativo")
            stack.append(math.sqrt(x))

        elif token == "log":
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para log")
            x = stack.pop()
            if x <= 0:
                raise RPNError("Log indefinido para ese valor")
            stack.append(math.log10(x))

        elif token == "ln":
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para ln")
            x = stack.pop()
            if x <= 0:
                raise RPNError("Ln indefinido para ese valor")
            stack.append(math.log(x))
        
        elif token == "exp":  # e^x
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para exp")
            x = stack.pop()
            stack.append(math.exp(x))

        elif token == "pow10":  # 10^x
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para pow10")
            x = stack.pop()
            stack.append(10 ** x)

        elif token == "pow":  # x^y
            if len(stack) < 2:
                raise RPNError("Pila insuficiente para pow")
            y = stack.pop()
            x = stack.pop()
            stack.append(x ** y)

        elif token == "inv":  # 1/x
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para inv")
            x = stack.pop()
            if x == 0:
                raise RPNError("División por cero en inv")
            stack.append(1 / x)    

        elif token == "chs":
            if len (stack) < 1:
                raise RPNError("Pila insuficiente para chs")
            x=stack.pop()
            stack.append(-x)    


        # =========================================
        # FUNCIONES TRIGONOMÉTRICAS
        # =========================================

        elif token == "sin":
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para sin")
            x = stack.pop()
            stack.append(math.sin(math.radians(x)))

        elif token == "cos":
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para cos")
            x = stack.pop()
            stack.append(math.cos(math.radians(x)))

        elif token == "tg":
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para tg")
            x = stack.pop()
            stack.append(math.tan(math.radians(x)))

        # =========================================
        # FUNCIONES INVERSAS
        # =========================================

        elif token == "asin":
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para asin")
            x = stack.pop()
            if x < -1 or x > 1:
                raise RPNError("asin fuera de dominio")
            stack.append(math.degrees(math.asin(x)))

        elif token == "acos":
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para acos")
            x = stack.pop()
            if x < -1 or x > 1:
                raise RPNError("acos fuera de dominio")
            stack.append(math.degrees(math.acos(x)))

        elif token == "atan":
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para atan")
            x = stack.pop()
            stack.append(math.degrees(math.atan(x)))


        # =========================================
        # MEMORIAS (RCL / STO)
        # =========================================

        elif token == "STO":
            if len(stack) < 2:
                raise RPNError("Pila insuficiente para STO")
            key = str(int(stack.pop())).zfill(2)
            value = stack[-1]
            if key not in memoria:
                raise RPNError("Memoria inválida")
            memoria[key] = value

        elif token == "RCL":
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para RCL")
            key = str(int(stack.pop())).zfill(2)
            if key not in memoria:
                raise RPNError("Memoria inválida")
            stack.append(memoria[key])

        # OPERADORES BINARIOS
        
        elif token in ["+", "-", "*", "/"]:
            if len(stack) < 2:
                raise RPNError("Pila insuficiente para operar")

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                resultado = a + b
            elif token == "-":
                resultado = a - b
            elif token == "*":
                resultado = a * b
            elif token == "/":
                if b == 0:
                    raise RPNError("División por cero")
                resultado = a / b

            stack.append(resultado)

        # NÚMEROS
        
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise RPNError(f"Token inválido: {token}")

    # VALIDACIÓN FINAL

    if len(stack) != 1:
        raise RPNError("La expresión no es válida (sobran elementos en la pila)")

    return stack[0]

def main():
    try:
        expresion = input("Ingrese expresión RPN: ")
        resultado = evaluar_rpn(expresion)
        print("Resultado:", resultado)
    except RPNError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()