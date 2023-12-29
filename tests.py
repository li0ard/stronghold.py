import unittest

from stronghold import *

class TestPointIntersection(unittest.TestCase):
	def test_getPointIntersection(self):
		a = Point(-240, 102, 132, 32.8)
		b = Point(-1020, 102, 1008, -7.2)

		res = getPointIntersection(a, b)
		self.assertEqual(round(res[0]), -985)
		self.assertEqual(round(res[1]), 1288)

class TestLineIntersectionOnCircle(unittest.TestCase):
	def test_getLineIntersectionOnCircle(self):
		a = Point(-240, 102, 132, 32.8)
		res = getLineIntersectionOnCircle(a, 216)
		self.assertEqual(round(res[0]), -130)
		self.assertEqual(round(res[1]), 172)

class TestCheckInRing(unittest.TestCase):
	def test_checkInRing(self):
		a = Point(-240, 102, 132, 32.8)
		b = Point(-1020, 102, 1008, -7.2)

		res = getPointIntersection(a, b)
		self.assertEqual(checkInRing(Point(res[0], 0, res[1], 0)), True)

class TestX4Z4Rule(unittest.TestCase):
	def test_applyX4Z4Rule(self):
		a = Point(-240, 102, 132, 32.8)
		b = Point(-1020, 102, 1008, -7.2)
		res = getPointIntersection(a, b)

		res2 = applyX4Z4Rule(Point(res[0], 0, res[1], 0))

		self.assertEqual(res2[0], -988.0)
		self.assertEqual(res2[1], 1284.0)

if __name__ == '__main__':
	unittest.main()
