# MANIPULATING DATETIME
from datetime import date, timedelta

today_date = date.today()

print("CURRENT DAY : ", today_date)

# as said earlier it takes argument as day by default
td = timedelta(5)
print("AFTER 5 DAYS DATE WILL BE : ", today_date + td)
print("BEFORE 5 DAYS DATE WILL BE : ", today_date - td)
