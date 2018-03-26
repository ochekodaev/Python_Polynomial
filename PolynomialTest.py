import unittest
from Polynomial import Polynomial




class PolynomialTest(unittest.TestCase):
    def test_ListTypeError(self):
        self.assertRaises(TypeError, Polynomial, "a")
        self.assertRaises(TypeError, Polynomial, 1)
        self.assertRaises(TypeError, Polynomial, 1.0)


    def test_EmptyListError(self):
        self.assertRaises(TypeError, Polynomial, [])


    def test_ListElementsTypeError(self):
        self.assertRaises(TypeError, Polynomial, ["a"])
        self.assertRaises(TypeError, Polynomial, ["a", 1, 1.0])
        self.assertRaises(TypeError, Polynomial, [1, "a", 1.0])
        self.assertRaises(TypeError, Polynomial, [1, 1.0, "a"])


    def test_CorrectInit_1(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p.coeffs, [1, 2, 3])
        self.assertEqual(p.degree, 2)


    def test_CorrectInit_2(self):
        p = Polynomial([1.0, 2.2, 3.1])
        self.assertEqual(p.coeffs, [1.0, 2.2, 3.1])
        self.assertEqual(p.degree, 2)


    def test_CorrectInit_3(self):
        p = Polynomial([1.0])
        self.assertEqual(p.coeffs, [1.0])
        self.assertEqual(p.degree, 0)


    def test_CorrectInit_4(self):
        p = Polynomial([0, 1.0, 5, 0])
        self.assertEqual(p.coeffs, [1.0, 5, 0])
        self.assertEqual(p.degree, 2)


    def test_CorrectInit_5(self):
        p = Polynomial([0, 0, 0, 0])
        self.assertEqual(p.coeffs, [0])
        self.assertEqual(p.degree, 0)


    def test_EqTypeError(self):
        p = Polynomial([0, 1.0, 5, 0])
        self.assertRaises(TypeError, p.__eq__, "a")


    def test_EqTruePolynom(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2, 3])
        self.assertTrue(p1 == p2)


    def test_EqFalsePolynom(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 3])
        self.assertFalse(p1 == p2)


    def test_EqTrueConst(self):
        p1 = Polynomial([1])
        p2 = 1
        self.assertTrue(p1 == p2)


    def test_EqFalseConst(self):
        p1 = Polynomial([1])
        p2 = 2
        self.assertFalse(p1 == p2)


    def test_AddPolynomTypeError(self):
        self.assertRaises(TypeError, Polynomial.__add__, Polynomial([1,2]), "a")


    def test_AddPolynom_1(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([3, 4])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [4, 6])
        self.assertEqual(p3.degree, 1)


    def test_AddPolynom_2(self):
        p1 = Polynomial([2])
        p2 = Polynomial([-3.5, 4])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [-3.5, 6])
        self.assertEqual(p3.degree, 1)


    def test_AddPolynom_3(self):
        p1 = Polynomial([2.0, 5.5, 1])
        p2 = Polynomial([-3.5, 4])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [2.0, 2.0, 5])
        self.assertEqual(p3.degree, 2)


    def test_AddConst_1(self):
        p1 = 1
        p2 = Polynomial([-3.5, 4])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [-3.5, 5])
        self.assertEqual(p3.degree, 1)


    def test_AddConst_2(self):
        p1 = Polynomial([2, 5.5, 1.0])
        p2 = 1.0
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [2, 5.5, 2.0])
        self.assertEqual(p3.degree, 2)


    def test_MultPolynomTypeError(self):
        self.assertRaises(TypeError, Polynomial.__mul__, Polynomial([1,2]), "a")


    def test_MultPolynom_1(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([3, 4])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [3, 10, 8])
        self.assertEqual(p3.degree, 2)


    def test_MultPolynom_2(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([-1, 2, 0])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [-1, 0, 4, 0])
        self.assertEqual(p3.degree, 3)


    def test_MultPolynom_3(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [1, 4, 7, 6])
        self.assertEqual(p3.degree, 3)


    def test_MultConst_1(self):
        p1 = 2
        p2 = Polynomial([1, 4])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [2, 8])
        self.assertEqual(p3.degree, 1)


    def test_MultConst_2(self):
        p1 = Polynomial([2, 1, 1])
        p2 = -2
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [-4, -2, -2])
        self.assertEqual(p3.degree, 2)

    
    def test_Str_1(self):
        p1 = Polynomial([1, 2])
        self.assertEqual(str(p1), "x+2")


    def test_Str_2(self):
        p1 = Polynomial([0, 0])
        self.assertEqual(str(p1), "0")


    def test_Str_3(self):
        p1 = Polynomial([0.0])
        self.assertEqual(str(p1), "0.0")


    def test_Str_4(self):
        p1 = Polynomial([-1.2, 2, 0])
        self.assertEqual(str(p1), "-1.2x2+2x")


    def test_Str_5(self):
        p1 = Polynomial([1, 2, -3, 4])
        self.assertEqual(str(p1), "x3+2x2-3x+4")


    def test_Str_6(self):
        p1 = Polynomial([0, 0, -3, 4])
        self.assertEqual(str(p1), "-3x+4")


    def test_Str_7(self):
        p1 = Polynomial([1, 2, 0, 4])
        self.assertEqual(str(p1), "x3+2x2+4")


if __name__ == "__main__":
    unittest.main()