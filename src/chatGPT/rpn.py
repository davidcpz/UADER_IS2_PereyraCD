def evaluar_rpn(expresion):
    stack = []
    tokens = expresion.split()

    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                resultado = a + b
            elif token == "-":
                resultado = a - b
            elif token == "*":
                resultado = a * b
            elif token == "/":
                resultado = a / b

            stack.append(resultado)
        else:
            stack.append(float(token))

    return stack[0]


def main():
    expresion = input("Ingrese expresión RPN: ")
    resultado = evaluar_rpn(expresion)
    print("Resultado:", resultado)


if __name__ == "__main__":
    main()