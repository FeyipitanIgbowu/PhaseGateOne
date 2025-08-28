import unittest
import checkout_app

class TestCustomerName(unittest.TestCase):
	def test_for_invalid_data_type(self):
		self.assertRaises(ValueError,checkout_app.customer_name,10)
		
	def test_function_works(self):
		response = checkout_app.customer_name("Feyi")
		self.assertEqual(response, "Hello Feyi")


class TestItemPrice(unittest.TestCase):
	def test_for_invalid_data_type(self):
		self.assertRaises(ValueError,checkout_app.item_price,"Hola", "Feyi")

	def test_for_negative_input(self):
		self.assertRaises(ValueError,checkout_app.item_price,-1, -3)
		
	def test_for_zero_input(self):
		self.assertRaises(ValueError,checkout_app.item_price,0 , 0)
		
	def test_function_works(self):
		response = checkout_app.item_price(2, 500)
		self.assertEqual(response, 1000)
		
class TestDiscount(unittest.TestCase):
	def test_for_invalid_data_type(self):
		self.assertRaises(ValueError,checkout_app.discount,"Hola", "Feyi")
		
	def test_for_negative_input(self):
		self.assertRaises(ValueError,checkout_app.discount,-1, -3)
		
	def test_for_zero_input(self):
		self.assertRaises(ValueError,checkout_app.discount,0 , 0)
		

	
		
		

