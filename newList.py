class Employee:
    def  __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.next = None

    def get_data(self):
        return self
    def set_next(self,ob):
        self.next = ob
    def get_next(self):
        return self.next
    def __str__(self):
        return self.name + " = "+str(self.roll)

class SinglyIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            #item = Employee("ccc",3)
            item = self.current.get_data()
            self.current = self.current.get_next()
            return item

class Singly:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return SinglyIterator(self.head)

    def insert(self, name,roll):
        new_node = Employee(name,roll)
        new_node.set_next(self.head) #"aaa",1  -> None
        self.head = new_node         # head = aaa
test_list = Singly()
test_list.insert("aaa",1)
test_list.insert("bbb",2)
test_list.insert("ccc",3)

for item in test_list:
    print(item)
