from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().sumar(""),0,"Cadena vacia")


    def test_sumar_unacadena(self):
        self.assertEqual(Calculadora().sumar("1"), 1, "un numero")



    def test_sumar_cadenaConUnNumero(self):
        self.assertEqual(Calculadora().sumar("1"), 1, "un numero")
        self.assertEqual(Calculadora().sumar("2"), 2, "un numero")


    def test_sumar_unacadenaConDosNumeros(self):
        self.assertEqual(Calculadora().sumar("1,3"), 4, "dos numeros")


    def test_sumar_unacadenaConMultiplesNumeros(self):
        self.assertEqual(Calculadora().sumar("5,2,4,1"), 12, "Multiples numeros")


    def test_sumar_unacadenaConMultiplesNumerosConSeparadores(self):
        self.assertEqual(Calculadora().sumar("5,2&4:1:2&8"), 22, "Multiples numeros distintos separadores")