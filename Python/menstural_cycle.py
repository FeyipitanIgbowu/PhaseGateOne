from datetime import datetime, timedelta
import calendar

def date_collection(month_name, day_number):
	if type(month_name) != str or type(day_number) != int:
		raise ValueError("Invalid Data Type")
		
	if day_number <= 0:
		raise ValueError("Zero's and negative numbers are not allowed")
		
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	month_name = month_name.strip().capitalize()
	if month_name not in months:
		raise ValueError("Invalid Month")
		
	year = 2025
	month_index = months.index(month_name) + 1
	highest_days = calendar.monthrange(year, month_index)[1]
	if day_number < 1 or day_number > highest_days:
		raise ValueError("Invalid Day")

	date_conversion = month_name + " " + str(day_number) + " 2025"  
	return datetime.strptime(date_conversion,"%B %d %Y")

def check_next_period(start_date, cycle_length):
	if type(start_date) != int or type(cycle_length) != int:
		raise ValueError("Invalid Data Type")
		
	if start_date <= 0 or cycle_length <= 0:
		raise ValueError("Zero's and negative numbers are not allowed")
	
	start_date = datetime.today().replace(day=start_date)
	next_period = start_date + timedelta(days=cycle_length)
	return next_period.day
	
def ovulation_date(start_date, cycle_length):
	if type(start_date) != int or type(cycle_length) != int:
		raise ValueError("Invalid Data Type")
	
	if start_date <= 0 or cycle_length <= 0:
		raise ValueError("Zero's and negative numbers are not allowed")
	
	start_date = datetime.today().replace(day=start_date)
	ovulation_date = start_date + timedelta(days=(cycle_length - 14))
	return ovulation_date.day
	
def fertile_window(start_date, cycle_length):
	start_date = datetime.today().replace(day=start_date)
	ovulation_date = start_date + timedelta(days=(cycle_length - 14))
	
	fertile_window = ovulation_date - timedelta(days=2), ovulation_date + timedelta(days=2)
    
    
    
    
    