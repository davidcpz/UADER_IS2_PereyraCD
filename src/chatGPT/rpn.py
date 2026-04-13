class RPNError(Exception):
    pass


def evaluar_rpn(expresion):
    stack = []
    tokens = expresion.split()

    for token in tokens:

        # Comandos de pila
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

        # Operadores
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

        # Números
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise RPNError(f"Token inválido: {token}")

    # Validación final
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