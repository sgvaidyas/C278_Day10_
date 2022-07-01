from datetime import datetime,timedelta
#x = 'December 1, 2021, 12:04:00 PM'
#y =datetime.strptime(x,'%B %d, %Y, %H:%M:%S %p')
x = 'December 1, 2021, 12:04:00 PM'
currentdate=datetime.strptime(x,'%B %d, %Y, %I:%M:%S %p')
new_datetime = timedelta(days = 5,minutes = 30, hours = 3)
different=currentdate - new_datetime
print("BEFORE 5 DAYS DATE WILL BE : ", currentdate - new_datetime)
print("BEFORE 5 DAYS DATE WILL BE : ",different.strftime('%B %d, %Y, %I:%M:%S %p'))
