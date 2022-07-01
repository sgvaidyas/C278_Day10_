class Employee:
    def  __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def __str__(self):
        return self.name + " = "+str(self.roll)

ob =  Employee("Aaaa",11)
ob2=  Employee("bbbb",22)
ob3 = Employee("ccc",33)
list_emp = [ob,ob2,ob3]
obs = iter(list_emp)
for emp in obs:
    print(emp)
"""
try:
    print(next(obs))
    print(next(obs))
    print(next(obs))
    print(next(obs))
except StopIteration:
    print("No more employees")
"""
