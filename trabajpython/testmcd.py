import unittest
from mcd import mcdcuatronumeros

class TestMCDCuatroNumeros(unittest.TestCase):

    def test_mcd_positivos_iguales(self):
        nro1 = nro2 = nro3 = nro4 = 12
        mcd_esperado = 12
        mcd_obtenido = mcdcuatronumeros(nro1, nro2, nro3, nro4)
        self.assertEqual(mcd_esperado, mcd_obtenido, "MCD de números positivos iguales no es correcto")

    def test_mcd_positivos_distintos(self):
        nro1 = 18
        nro2 = 36
        nro3 = 54
        nro4 = 27
        mcd_esperado = 9
        mcd_obtenido = mcdcuatronumeros(nro1, nro2, nro3, nro4)
        self.assertEqual(mcd_esperado, mcd_obtenido, "MCD de números positivos distintos no es correcto")

    def test_mcd_con_cero(self):
        nro1 = 18
        nro2 = 36
        nro3 = 0
        nro4 = 27
        mcd_esperado = 9
        mcd_obtenido = mcdcuatronumeros(nro1, nro2, nro3, nro4)
        self.assertEqual(mcd_esperado, mcd_obtenido, "MCD con cero no es correcto")

    def test_mcd_negativos(self):
        nro1 = -18
        nro2 = -36
        nro3 = -54
        nro4 = -27
        mcd_esperado = 9
        mcd_obtenido = mcdcuatronumeros(nro1, nro2, nro3, nro4)
        self.assertEqual(mcd_esperado, mcd_obtenido, "MCD con números negativos no es correcto")

if __name__ == "__main__":
    unittest.main()