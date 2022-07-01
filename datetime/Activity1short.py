from datetime import datetime,timedelta
delta1 = timedelta(days=3, seconds=0,
    minutes=15,
    hours=5,
)
delta2 = timedelta(
    days=7,
    seconds=10,
    minutes=50,
    hours=20,
)
sumdelta = delta1 + delta2
print(sumdelta.days)
print(sumdelta/timedelta(seconds=1))
print(sumdelta/timedelta(minutes=1))
print(sumdelta/timedelta(hours=1))

print("Minutes = ",sumdelta.total_seconds()//60)
