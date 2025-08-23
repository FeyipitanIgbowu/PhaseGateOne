import java.util.Scanner;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class MensturalCycleApp {

public static int dateCollection(int monthNumber, int dayNumber){
  String[] months = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
  int year = 2025;
   
String dateString = monthName + " " + dayNumber + " " + year;
DateTimeFormatter input = DateTimeFormatter.ofPattern("MM d");
LocalDate date = LocalDate.parse(dateString, input);

return date.toString();
}

public static void main(String... feyi) {
 Scanner input = new Scanner(System.in);
 
 System.out.print("Enter the Month: ");
 int month = input.nextInt();
 
 System.out.print("Enter the Day Starting Day of your Last Period: ");
 int day = input.nextInt();
 System.out.print(dateCollection(month, day));


}

}