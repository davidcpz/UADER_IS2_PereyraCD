import unittest

from rpn import evaluar_rpn, RPNError


class TestRPN(unittest.TestCase):

    # Operaciones básicas
    def test_suma(self):
        self.assertEqual(evaluar_rpn("3 4 +"), 7)

    def test_resta(self):
        self.assertEqual(evaluar_rpn("5 2 -"), 3)

    def test_multiplicacion(self):
        self.assertEqual(evaluar_rpn("3 3 *"), 9)

    def test_division(self):
        self.assertEqual(evaluar_rpn("8 2 /"), 4)

    # Funciones
    def test_sqrt(self):
        self.assertEqual(evaluar_rpn("9 sqrt"), 3)

    def test_log(self):
        self.assertEqual(evaluar_rpn("100 log"), 2)

    # Constantes
    def test_pi(self):
        self.assertAlmostEqual(evaluar_rpn("p"), 3.1415, places=3)

    # Comandos de pila
    def test_dup(self):
        self.assertEqual(evaluar_rpn("3 dup +"), 6)

    # Errores
    def test_error_pila(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 +")

    def test_division_cero(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 0 /")

    def test_token_invalido(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 a +")

    def test_expresion_invalida(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 4")


if __name__ == "__main__":
    unittest.main()