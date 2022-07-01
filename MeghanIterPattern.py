class AddendSeq:
    def __init__(self):
        num = int(input("Enter a whole number: "))
        self.num = num

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        self.a+=1
        if self.a == self.num//2+1 and self.num%2==1:
                return str(self.a)
        if self.a < self.num//2+1:
            return str(self.num-self.a+1) + "   "+str(self.a)+"  "
        else:
            raise StopIteration

numbers = AddendSeq()
numbers_iterator = iter(numbers)

for x in numbers_iterator :
    print(x, end="")
