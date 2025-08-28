const prompt = require('prompt-sync')();

function CheckoutApp {
let name = prompt("Customer's Name: ");
	
	
let cashierName = prompt("Cashier's Name: ");
	let itemsBought = "";
	let total = 0;
	let extraGoods = "Yes";
		while(extraGoods.equalsIgnoreCase("Yes")) {
		let item = prompt("What did the user buy?: ");
				
		let quantity = prompt("How many pieces?: ");
		
		let price = prompt("How much per unit?: ");
		
		let subTotal = quantity * price;
		total += subTotal;
		
		let extraGoods = prompt("Add More Items?: ");
	
		itemsBought = item + "-" + quantity + "x" + price + "=" + subTotal;
				
	let discount = prompt("How much discount will he get?: ");
		}
		
	let storeName = "SEMICOLON STORES";
	let storeBranch = "MAIN BRANCH";
	let storeLocation = "312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.";
	let storeNumber = "09053293671";
	let date = "18-Dec-22 8:48:11 pm";
	
	let discount = total * 0.1;
	let vat = total * 0.075;
	let grandTotal = total - discount + vat;
	
	console.log(storeName);
	console.log(storeBranch);
	console.log(storeNumber);
	console.log(date);
	console.log("--------------------------------------------------------------------------");
	console.log("--------------------------------------------------------------------------");
	console.log("               ITEM 		QTY		PRICE			TOTAL(NGN)	 ");
	console.log("--------------------------------------------------------------------------");
	


}
}
