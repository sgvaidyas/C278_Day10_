class SeqDiv3:
    def __iter__(self):
        self.a = 3
        return self
    def __next__(self):
        if (self.a < 20):
            x =self.a
            self.a +=3
            return x
        raise StopIteration

numbers = SeqDiv3()
for number in numbers: # this will stop at 18 because we implemented StopIteration.
    print(number)
