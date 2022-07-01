class SeqDiv3:
    def __iter__(self):
        self.a = 3
        return self
    def __next__(self):
        if (self.a < 20):
            x = self.a
            self.a += 3
            return x
        raise StopIteration
numbers = SeqDiv3()
numbers_iterator = iter(numbers)
try:
    print(next(numbers_iterator)) # display number 3
    print(next(numbers_iterator)) # display number 6
    print(next(numbers_iterator)) # display number 9
    print(next(numbers_iterator)) # display number 12
    print(next(numbers_iterator)) # display number 15
    print(next(numbers_iterator)) # display number 18
    print(next(numbers_iterator)) # error because we passed 20 (because 18+3 is 21)
except StopIteration:
    print("You reached end of iteration")
