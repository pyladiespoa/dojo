# extensoTest.py

import unittest
from extenso import *

class ExtensoTest(unittest.TestCase):

	def testORetornaZeroReais(self):
		self.assertEquals("Zero reais", extenso(0))

	def test1RetornaUmReal(self):
		self.assertEquals("Um real", extenso(1))

	def test2RetornaDoisReais(self):
		self.assertEquals("Dois reais", extenso(2))

	def test3RetornaTresReais(self):
		self.assertEquals("Tres reais", extenso(3))

	def test4RetornaTresReais(self):
		self.assertEquals("Quatro reais", extenso(4))

	def test5RetornaCincoReais(self):
		self.assertEquals("Cinco reais", extenso(5))

	def testMenos1NaoDeveDarErro(self):
		self.assertEquals("", extenso(-1))

	def testUmaStringNaoDeveDarErro(self):
		self.assertEquals("", extenso("Batata"))

	def testNoneNaoDeveDarErro(self):
		self.assertEquals("", extenso(None))

	def testUmaListaNaoDeveDarErro(self):
		self.assertEquals("", extenso([]))

	def test19ponto01RetornaDezenoveReaiseUmCentavo(self):
		self.assertEquals("Dezenove reais e um centavo", extenso(19.01))

	def test9ponto9RetornaNoveReaiseNoveCentavos(self):
		self.assertEquals("Nove reais e nove centavos", extenso(9.09))

	def test0ponto10RetornaDezCentavos(self):
		self.assertEquals("Dez centavos", extenso(0.10))

	def test1ponto12RetornaUmRealEDozeCentavos(self):
		self.assertEquals("Um real e doze centavos", extenso(1.12))

	def test0ponto8RetornaOitentaCentavos(self):
		self.assertEquals("Oitenta centavos", extenso(0.80))

	def test0ponto4RetornaQuarentaCentavos(self):
		self.assertEquals("Quarenta centavos", extenso(0.40))

	def test2ponto5RetornaDoisReaiseCinquentaCentavos(self):
		self.assertEquals("Dois reais e cinquenta centavos", extenso(2.50))

	def test1ponto6RetornaUmReale60Centavos(self):
		self.assertEquals("Um real e sessenta centavos", extenso(1.60))

unittest.main()