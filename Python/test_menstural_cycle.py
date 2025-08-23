import unittest
from datetime import datetime, timedelta
import menstural_cycle

class TestDateCollection(unittest.TestCase):
	def test_for_invalid_data_type_of_date(self):
		self.assertRaises(ValueError,menstural_cycle.date_collection,23, "Feyi")
		
	def test_for_invalid_data_type_of_month(self):
		self.assertRaises(ValueError,menstural_cycle.date_collection,"Feyi", 23)

	def test_for_zero_input(self):
		self.assertRaises(ValueError,menstural_cycle.date_collection, "Febuarry", 0)

	def test_for_negative_input(self):
		self.assertRaises(ValueError,menstural_cycle.date_collection, "Febuarry", -1)

	def test_for_wrong_month_input(self):
		self.assertRaises(ValueError,menstural_cycle.date_collection, "Febuarry", 23)

	def test_for_invalid_date_in_february(self):
		self.assertRaises(ValueError,menstural_cycle.date_collection, "Febuarry", 30)

	def test_that_the_function_works(self):
		response = menstural_cycle.date_collection("September", 1)
		expected = datetime(2025, 9, 1)
		self.assertEqual(response, expected)
		
class TestForNextPeriod(unittest.TestCase):
	def test_for_invalid_data_type_for_cycle_length(self):
		self.assertRaises(ValueError,menstural_cycle.check_next_period,20 , "Feyi")
	
	def test_for_invalid_data_type_for_start_date(self):
		self.assertRaises(ValueError,menstural_cycle.check_next_period, "Feyi", 10)

	def test_for_zero_error(self):
		self.assertRaises(ValueError,menstural_cycle.check_next_period,0 , 0)
		
	def test_for_negative_input(self):
		self.assertRaises(ValueError,menstural_cycle.check_next_period, -1 , -5)
	
	def test_that_function_works(self):
		response = menstural_cycle.check_next_period(1, 27)
		self.assertEqual(response, 28)
		
class TestForOvulationDate(unittest.TestCase):
	def test_for_invalid_data_type_for_cycle_length(self):
		self.assertRaises(ValueError,menstural_cycle.ovulation_date,20 , "Feyi")
	
	def test_for_invalid_data_type_for_start_date(self):
		self.assertRaises(ValueError,menstural_cycle.ovulation_date, "Feyi", 1)

	def test_for_zero_error(self):
		self.assertRaises(ValueError,menstural_cycle.ovulation_date,0 , 0)
		
	def test_for_negative_input(self):
		self.assertRaises(ValueError,menstural_cycle.ovulation_date, -1 , -5)
	
	def test_that_function_works(self):
		response = menstural_cycle.ovulation_date(1, 27)
		self.assertEqual(response, 14)

	