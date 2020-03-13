from unittest import TestCase

import conexion


class Test(TestCase):
    """
    test de valido_dni
    """
    def test_valido_dni(self):
        from funcionescli import validoDNI
        self.assertTrue(validoDNI("39513462Z"))

