class SeqDiv3:
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        self.a += 3
        return self.a
numbers = SeqDiv3()
numbers_iterator = iter(numbers)
print(numbers_iterator)
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
print(next(numbers_iterator))
