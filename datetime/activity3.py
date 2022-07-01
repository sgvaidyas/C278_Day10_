from datetime import datetime, timedelta
start = input("Please enter a start date in the format DD/MM/YY:\n")
end = input("Please enter an end date in the format DD/MM/YY:\n")
try:
    start_date = datetime.strptime(start, '%d/%m/%y')
    end_date = datetime.strptime(end, '%d/%m/%y')
except Exception as e:
    print(e)
else:
    delta = end_date-start_date
    print()
    print("Between the start and end date, the time elapsed is:")
    print(str(delta.days//365)+"years", str(delta.days%365//30)+"months", str(delta.days%365%30)+"days")
years   = delta.days//365
months  = delta.days//30
days    = delta.days%365%30
print("Total months = ", months," days = ",days)
print("Total weeks = ", delta.days//7," days = ",delta.days%7)


print("SEC = " ,delta/timedelta(seconds=1))
print("MINS = ",delta/timedelta(minutes=1))
print("HOURS" , delta/timedelta(hours=1))
# September 1, 1994 and the end date December 1, 2021
# 01/09/94  01/12/21
