import java.util.Scanner;
import java.util.Arrays;

public class StudentGradeApp {
	public static void main(String... feyi) {
	Scanner input = new Scanner(System.in);

System.out.println("How many students do you have?: ");
int studentNumber = input.nextInt();

System.out.println("How many subjects do they offer?: ");
int subjects = input.nextInt();

System.out.println("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>");
System.out.println("Saved Successfully");

int [][] studentScores = new int[studentNumber][subjects];
int totalScore = 0;
int classTotal = 0;
int pupilNumber = 0;

for(int count = 0; count < studentScores.length; count++) {
	for(int counter = 0; counter < studentScores[count].length; counter++) {
		System.out.println("Entering score for Student: ");
		System.out.println("Enter score for subject: ");
		int subjectNumber = input.nextInt();
		
		while(subjectNumber < 0 || subjectNumber > 100) {
		System.out.print("Enter score for subject: ");
		subjectNumber = input.nextInt();
		}
	studentScores[count][counter]= subjectNumber;
	classTotal += counter;
	pupilNumber += counter;

}
}
System.out.print(Arrays.deepToString(studentScores));
Double averageScore = classTotal / pupilNumber;


































}
}