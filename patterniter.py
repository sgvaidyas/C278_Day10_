class SeqDiv3:
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        self.a = self.n
        self.start=1
        self.even=False
        return self
    def __next__(self):
        if(self.a<self.start):
            raise StopIteration
        if (self.even==True):
            self.start+=1
            return self.start-1
        else:
            self.a-=1
            return self.a+1

numbers = SeqDiv3(8)
numbers_iterator = iter(numbers)
for x in numbers_iterator:
    print(x)
