import unittest
from rpn import evaluar_rpn, RPNError


class TestRPN(unittest.TestCase):

    # =========================
    # OPERACIONES BÁSICAS
    # =========================
    def test_suma(self):
        self.assertEqual(evaluar_rpn("3 4 +"), 7)

    def test_resta(self):
        self.assertEqual(evaluar_rpn("5 2 -"), 3)

    def test_multiplicacion(self):
        self.assertEqual(evaluar_rpn("3 3 *"), 9)

    def test_division(self):
        self.assertEqual(evaluar_rpn("8 2 /"), 4)

    # =========================
    # FUNCIONES MATEMÁTICAS
    # =========================
    def test_sqrt(self):
        self.assertEqual(evaluar_rpn("9 sqrt"), 3)

    def test_log(self):
        self.assertEqual(evaluar_rpn("100 log"), 2)

    def test_ln(self):
        self.assertAlmostEqual(evaluar_rpn("1 ln"), 0, places=3)

    def test_exp(self):
        self.assertAlmostEqual(evaluar_rpn("1 exp"), 2.718, places=2)

    def test_pow10(self):
        self.assertEqual(evaluar_rpn("2 pow10"), 100)

    def test_pow(self):
        self.assertEqual(evaluar_rpn("2 3 pow"), 8)

    def test_inv(self):
        self.assertEqual(evaluar_rpn("4 inv"), 0.25)

    def test_chs(self):
        self.assertEqual(evaluar_rpn("5 chs"), -5)

    # =========================
    # CONSTANTES
    # =========================
    def test_pi(self):
        self.assertAlmostEqual(evaluar_rpn("p"), 3.1415, places=3)

    def test_e(self):
        self.assertAlmostEqual(evaluar_rpn("e"), 2.718, places=2)

    def test_phi(self):
        self.assertAlmostEqual(evaluar_rpn("j"), 1.618, places=2)

    # =========================
    # COMANDOS DE PILA
    # =========================
    def test_dup(self):
        self.assertEqual(evaluar_rpn("3 dup +"), 6)

    def test_swap(self):
        self.assertEqual(evaluar_rpn("3 4 swap -"), 1)

    def test_drop(self):
        self.assertEqual(evaluar_rpn("3 4 drop"), 3)

    def test_clear(self):
        self.assertEqual(evaluar_rpn("3 4 clear 5"), 5)

    # =========================
    # TRIGONOMETRÍA
    # =========================
    def test_sin(self):
        self.assertAlmostEqual(evaluar_rpn("90 sin"), 1, places=2)

    def test_cos(self):
        self.assertAlmostEqual(evaluar_rpn("0 cos"), 1, places=2)

    def test_tg(self):
        self.assertAlmostEqual(evaluar_rpn("45 tg"), 1, places=2)

    def test_asin(self):
        self.assertAlmostEqual(evaluar_rpn("1 asin"), 90, places=1)

    def test_acos(self):
        self.assertAlmostEqual(evaluar_rpn("1 acos"), 0, places=1)

    def test_atan(self):
        self.assertAlmostEqual(evaluar_rpn("1 atan"), 45, places=1)

    # =========================
    # MEMORIA
    # =========================
    def test_memoria(self):
        self.assertEqual(evaluar_rpn("5 0 STO drop 0 RCL"), 5)

    # =========================
    # ERRORES
    # =========================
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

    def test_sqrt_negativo(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("-4 sqrt")

    def test_log_invalido(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("0 log")

    def test_memoria_invalida(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("5 10 STO")

    # =========================
    # CASOS FALTANTES
    # =========================

    def test_ln_invalido(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("-1 ln")

    def test_pow10_negativo(self):
        self.assertEqual(evaluar_rpn("-1 pow10"), 0.1)

    def test_inv_cero(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("0 inv")

    def test_asin_fuera_rango(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("2 asin")

    def test_acos_fuera_rango(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("2 acos")

    def test_rcl_memoria_vacia(self):
    # memoria 09 nunca usada → debería devolver 0
        self.assertEqual(evaluar_rpn("9 RCL"), 0)

    def test_clear_vacio(self):
        self.assertEqual(evaluar_rpn("clear 3"), 3)

    def test_swap_error(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("3 swap")

    def test_drop_error(self):
        with self.assertRaises(RPNError):
            evaluar_rpn("drop")

    
if __name__ == "__main__":
    unittest.main()