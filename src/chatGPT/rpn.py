import math

# ==========================================================
# MEMORIAS (00–09)
# Estructura global que simula registros de memoria tipo calculadora.
# Se utiliza un diccionario con claves "00" a "09".
# ==========================================================

memoria = {f"{i:02}": 0 for i in range(10)}


# ==========================================================
# EXCEPCIÓN PERSONALIZADA
# Se utiliza para manejar todos los errores del evaluador RPN
# de manera controlada y uniforme.
# ==========================================================
class RPNError(Exception):
    """Excepcion personalizada para errores en la evaluación RPN."""
    pass


# ==========================================================
# FUNCIÓN PRINCIPAL DE EVALUACIÓN RPN
# Recibe una expresión en notación polaca inversa (string)
# y la evalúa utilizando una pila (stack).
# ==========================================================
def evaluar_rpn(expresion):

    # Validación de entrada vacía
    if not expresion.strip():
        raise RPNError("Expresión vacía")

    # Reinicio de memoria en cada ejecución
    global memoria
    memoria = {f"{i:02}": 0 for i in range(10)}

    # Pila principal donde se almacenan los operandos
    stack = []

    # Separación de la expresión en tokens
    tokens = expresion.split()

    # Recorrido secuencial de cada token
    for token in tokens:

        # Permite usar comandos en mayúsculas o minúsculas
        token = token.lower()

        # ==================================================
        # COMANDOS DE PILA
        # Manipulan directamente la estructura stack
        # ==================================================
        if token == "dup":
            # Duplica el último elemento
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para dup")
            stack.append(stack[-1])

        elif token == "swap":
            # Intercambia los dos últimos elementos
            if len(stack) < 2:
                raise RPNError("Pila insuficiente para swap")
            stack[-1], stack[-2] = stack[-2], stack[-1]

        elif token == "drop":
            # Elimina el último elemento
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para drop")
            stack.pop()

        elif token == "clear":
            # Limpia completamente la pila
            stack.clear()

        # ==================================================
        # CONSTANTES MATEMÁTICAS
        # Se agregan directamente a la pila
        # ==================================================
        elif token == "p":  # π
            stack.append(math.pi)

        elif token == "e":  # Número de Euler
            stack.append(math.e)

        elif token == "j":  # Número áureo (φ)
            stack.append((1 + 5**0.5) / 2)

        # ==================================================
        # FUNCIONES MATEMÁTICAS (UNARIAS Y BINARIAS)
        # Validan dominio y cantidad de operandos
        # ==================================================
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

        elif token == "exp":
            # Calcula e^x
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para exp")
            x = stack.pop()
            stack.append(math.exp(x))

        elif token == "pow10":
            # Calcula 10^x
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para pow10")
            x = stack.pop()
            stack.append(10**x)

        elif token == "pow":
            # Potencia x^y (binaria)
            if len(stack) < 2:
                raise RPNError("Pila insuficiente para pow")
            y = stack.pop()
            x = stack.pop()
            stack.append(x**y)

        elif token == "inv":
            # Inverso multiplicativo 1/x
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para inv")
            x = stack.pop()
            if x == 0:
                raise RPNError("División por cero en inv")
            stack.append(1 / x)

        elif token == "chs":
            # Cambio de signo
            if len(stack) < 1:
                raise RPNError("Pila insuficiente para chs")
            x = stack.pop()
            stack.append(-x)

        # ==================================================
        # FUNCIONES TRIGONOMÉTRICAS (GRADOS)
        # Conversión necesaria: grados → radianes
        # ==================================================
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

        # ==================================================
        # FUNCIONES INVERSAS (resultado en grados)
        # ==================================================
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

        # ==================================================
        # MEMORIAS (STO / RCL)
        # STO: guarda valor en memoria
        # RCL: recupera valor
        # ==================================================
        elif token == "STO":
            if len(stack) < 2:
                raise RPNError("Pila insuficiente para STO")

            # Se obtiene la clave de memoria desde la pila
            key = str(int(stack.pop())).zfill(2)

            # Se mantiene el valor en la pila (no se elimina)
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

        # ==================================================
        # OPERADORES BINARIOS
        # Requieren dos operandos en la pila
        # ==================================================
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

        # ==================================================
        # PARSEO DE NÚMEROS
        # Convierte token a float si no es operador/comando
        # ==================================================
        else:
            try:
                stack.append(float(token))
            except ValueError as e:
                raise RPNError(f"Token inválido: {token}") from e

    # ==================================================
    # VALIDACIÓN FINAL
    # Debe quedar exactamente un elemento en la pila
    # ==================================================
    if len(stack) != 1:
        raise RPNError("La expresión no es válida (sobran elementos en la pila)")

    return stack[0]


# ==========================================================
# FUNCIÓN MAIN
# Punto de entrada del programa
# ==========================================================
def main():
    try:
        expresion = input("Ingrese expresión RPN: ").strip()
        resultado = evaluar_rpn(expresion)
        print("Resultado:", resultado)
    except RPNError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
