import unittest
import menstural_cycle

class TestMensturalCycle(unittest.TestCase):
	def test_for_invalid_data_type_of_date_and_month(self):
		self.assertRaises(ValueError,menstural_cycle.date_collection,23, "Feyi")
		
	def test_for_zero_input(self):
		self.assertRaises(ValueError,menstural_cycle.date_collection, "Febuarry", 0)

	def test_for_negative_input(self):
		self.assertRaises(ValueError,menstural_cycle.date_collection, "Febuarry", -1)

	def test_for_wrong_month_input(self):
		self.assertRaises(ValueError,menstural_cycle.date_collection, "Febuarry", 23)

	def test_for_invalid_date_in_february(self):
		self.assertRaises(ValueError,menstural_cycle.date_collection, "Febuarry", 30)


