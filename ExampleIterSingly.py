class Employee:
    def  __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.next = None

    def __str__(self):
        return self.name + " = "+str(self.roll)

class Singly:
    def __init__(self):
        self.head=None
        self.ptr =None

    def insert(self,name,roll):
        temp = Employee(name,roll)
        if(self.head==None):
            self.head = temp
        else:
            temp.next=self.head
            self.head = temp

    def __iter__(self):
        self.ptr = self.head
        return self.ptr
    def __next__(self):
        if self.ptr == None:
            raise StopIteration
        self.ptr = self.ptr.next
        return self.ptr

ob = Singly()
ob.insert("aaaa",111)
ob.insert("bbbb",222)
ob.insert("cccc",333)
ob.insert("ddddd",444)
traverse = iter(ob)
print(next(traverse))
