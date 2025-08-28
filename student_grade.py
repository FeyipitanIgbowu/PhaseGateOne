student_no = input("How many students do you have?: ")
student_no = int(student_no)

subjects = input("How many subjects do they offer?: ")
subjects = int(subjects)	
print("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Saved Successfully")

student_scores = []
total_average = []
class_total = 0
pupil_no = 0
for student in range(student_no):
	mini_score = []
	for subject in range(subjects):
		print("Entering score for Student", student + 1)
		subject_no = int(input("Enter score for subject: "))
		mini_score.append(subject_no)
		while(subject_no < 0 or subject_no > 100):
			print("Invalid Number, only scores from 1-100 are allowed")
			print("Entering score for Student", student + 1)
			subject_no = int(input("Enter score for subject: "))
			mini_score.append(subject_no)
	student_scores.append(mini_score)
			               
for student in student_scores:
	for pupil in student:
		class_total += pupil      
		
for student in student_scores:
	for pupil in student:
		   pupil_no += pupil
		
average_score = class_total / pupil_no
#for pupil in student_scores:
	#maximum = print(max(pupil))
	                                                                                                                                                                                              
print(total_average)                  
print(student_scores)

	
print("CLASS SUMMARY")
print("=============================================================================================================")
print("Class total score is: ", class_total)
print("Class Average score is: ", average_score)
print("=============================================================================================================")











