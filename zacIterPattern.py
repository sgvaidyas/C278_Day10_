class SeqAlternate:
    def __init__(self,n):
      self.a = n
    def __iter__(self):
        self.b = 1
        self.flip = False
        return self
    def __next__(self):
        if self.a < self.b:
          raise StopIteration
        else:
          out = 0
          if self.flip:
            out = self.b
            self.b += 1
            self.flip = False
          else:
            out = self.a
            self.a -= 1
            self.flip = True
          return out


numbers = SeqAlternate(int(input("n?: ")))
numbers_iterator = iter(numbers)
for x in numbers_iterator :
    print(x, end=" ")
