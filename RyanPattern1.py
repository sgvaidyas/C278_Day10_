class Sequence:
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        self.a = self.n #8
        self.b = 1
        return self
    def __next__(self):
        if self.a >= self.b:
            user_generated = self.a
            increasing_inc = self.b
            self.a -= 1
            self.b += 1
            return [user_generated, increasing_inc]
        else:
            raise StopIteration
seq_obj = Sequence(8)
seq_iter = iter(seq_obj)
for x,y in seq_iter:
    if(x!=y):
        print (x,"\t" ,y,end="\t")
    else:
        print (x)
