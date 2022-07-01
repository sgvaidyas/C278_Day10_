class TimeCalculator:
    def __init__(self):
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        self.only_days = 0.0
        self.only_hours = 0.0
        self.only_minutes = 0.0
        self.only_seconds = 0

    def add(self):
        first_days = int(input("Enter the first number of days"))
        first_hours = int(input("Enter the first number of hours"))
        first_minutes = int(input("Enter the first number of minutes"))
        first_seconds = int(input("Enter the first number of seconds"))

        second_days = int(input("Enter the second number of days"))
        second_hours = int(input("Enter the second number of hours"))
        second_minutes = int(input("Enter the second number of minutes"))
        second_seconds = int(input("Enter the second number of seconds"))

        self.seconds = first_seconds + second_seconds
        self.minutes = first_minutes + second_minutes + self.seconds // 60
        self.seconds = self.seconds % 60
        self.hours = first_hours + second_hours + self.minutes // 60
        self.minutes = self.minutes % 60
        self.days = first_days + second_days + self.hours // 24
        self.hours = self.hours % 24

        self.only_days += first_days + second_days
        self.only_days += (first_hours + second_hours) / 24
        self.only_days += (first_minutes + second_minutes) / 60 /24
        self.only_days += (first_seconds + second_seconds) / 60 / 60 / 24

        self.only_hours += (first_days + second_days) * 24
        self.only_hours += first_hours + second_hours
        self.only_hours += (first_minutes + second_minutes) / 60
        self.only_hours += (first_seconds + second_seconds) / 60 / 60

        self.only_minutes += (first_days + second_days) * 24 * 60
        self.only_minutes += (first_hours + second_hours) * 60
        self.only_minutes += first_minutes + second_minutes
        self.only_minutes += (first_seconds + second_seconds) / 60

        self.only_seconds += (first_days + second_days) * 24 * 60 * 60
        self.only_seconds += (first_hours + second_hours) * 60 * 60
        self.only_seconds += (first_minutes + second_minutes) * 60
        self.only_seconds += first_seconds + second_seconds

        print("\nResults of your addition")
        self.display()

    def display(self):
        print("{} days {} hours {} minutes {} seconds".format(self.days, self.hours, self.minutes, self.seconds))
        print("{} days".format(self.only_days))
        print("{} hours".format(self.only_hours))
        print("{} minutes".format(self.only_minutes))
        print("{} seconds".format(self.only_seconds))

cal = TimeCalculator()
cal.add()
