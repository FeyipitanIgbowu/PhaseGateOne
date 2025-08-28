import java.util.Scanner;
public class CheckoutApp {
	public static void main(String... feyi) {
	Scanner input = new Scanner(System.in);


	System.out.print("Customer's Name: ");
	String name = input.nextLine();
	
	System.out.print("Cashier's Name: ");
	String cashierName = input.nextLine();

	String itemsBought = "";
	int total = 0;
	String extraGoods = "Yes";
		while(extraGoods.equalsIgnoreCase("Yes")) {
		System.out.print("What did the user buy?: ");
		String item = input.nextLine();
		
		System.out.print("How many pieces?: ");
		int quantity = input.nextInt();

		System.out.print("How much per unit?: ");
		int price = input.nextInt();
		
		int subTotal = quantity * price;
		total += subTotal;
		
		System.out.println("Add More Items?: ");
		extraGoods = input.nextLine();
	
		itemsBought = item + "-" + quantity + "x" + price + "=" + subTotal;
				
		System.out.print("How much discount will he get?: ");
		int discount = input.nextInt();
		}
		
	String storeName = "SEMICOLON STORES";
	String storeBranch = "MAIN BRANCH";
	String storeLocation = "312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.";
	String storeNumber = "09053293671";
	String date = "18-Dec-22 8:48:11 pm";
	
	double discount = total * 0.1;
	double vat = total * 0.075;
	double grandTotal = total - discount + vat;
	
	System.out.print(storeName);
	System.out.println(storeBranch);
	System.out.println(storeNumber);
	System.out.println(date);
	System.out.println("--------------------------------------------------------------------------");
	System.out.print("--------------------------------------------------------------------------");
	System.out.println("               ITEM 		QTY		PRICE			TOTAL(NGN)	 ");
	System.out.print("--------------------------------------------------------------------------");
	


}
}