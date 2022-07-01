class faebdc:
    a = 0
    b = 1
    def __iter__(self):
        self.a = int(input("n = "))
        while self.a >= self.b:#the pattern continues
            yield self.a
            if(self.a != self.b):
                yield self.b
            self.a -= 1
            self.b += 1
for x in iter(faebdc()) :
    print(x,end = "")
print()
