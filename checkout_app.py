def customer_name(alphabet):
	if type(alphabet) != str:
		raise ValueError("Alphabet expected")
	return "Hello" + " " + alphabet
	
def item_price(item_no, price):
	if type(item_no) != int and type(price) != int:
		raise ValueError("Number Expected")
		
	if item_no <= 0 or price <= 0:
		raise ValueError("Zero's and Negative Numbers are not Allowed")
	
	total_price = item_no * price
	return total_price
	vat = 17.50 / 100 * total_price
	return vat
def discount(discount_input , t_price):
	if type(discount_input) != int and type(t_price) != int:
		raise ValueError("Number Expected")

	if discount_input <= 0 or t_price <= 0:
		raise ValueError("Zero's and Negative Numbers are not Allowed")

	total_discount = (discount_input / t_price) * 100
	return total_discount
	

def main():		
	name = input("What is the Customer's Name: ")
	print(customer_name(name))	
	cashier_name = input("Cashier's Name: ")

	while (extra_goods == "Yes"):
		item = input("What did the user buy?: ")
		item_no = input("How many pieces?: ")
		price = input("How much per unit?: ")
		price = int(price)
		item_no = int(item_no)
		print(item_price(item_no, price))
		
		sub_total = quantity * price
		total += sub_total
	

	extra_goods = input("Add More Items?: ")

	discount_input = input("How much discount will he get?: ")
	discount_input = int(discount_input)
	
	t_price = item_price(item_no, price)

	print(discount(discount_input,t_price))
	
	t_vat = 17.50 * t_price / 100
	
	t_discount= discount(discount_input, t_price)
	bill = t_price + t_discount - t_vat
	
	
	store_name = 'SEMICOLON STORES'
	store_branch = 'MAIN BRANCH'
	store_location = '312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.'
	store_number = '09053293671'
	date = "18-Dec-22 8:48:11 pm"
	
	print(store_name)
	print(store_branch)
	print(store_location)
	print("Tel: ",store_number)
	print("Date: ",date)
	print("Customers Name: ", name)
	print("--------------------------------------------------------------------------")
	print("--------------------------------------------------------------------------")
	print("               ITEM 		QTY		PRICE			TOTAL(NGN)	 ")
	print("--------------------------------------------------------------------------")
	print("		", item,"	 	 ",item_no,"		",price,"		",t_price	)
	print("--------------------------------------------------------------------------")
	print("			 			 ","Sub Total:","			",t_price	)
	print("			 			 ","Discount:","				",t_discount)
	print("			 		","VAT @ 17.50%:","			",t_vat	)
	print("--------------------------------------------------------------------------")
	print("--------------------------------------------------------------------------")
	print("			 		","Bill Total:","			",bill		)
	print("--------------------------------------------------------------------------")
	print("--------------------------------------------------------------------------")
	print("	","THIS IS NOT AN RECIEPT KINDLY PAY", bill,"					")
	print("--------------------------------------------------------------------------")
	print("--------------------------------------------------------------------------")
	

if __name__ == "__main__":
	main()
		