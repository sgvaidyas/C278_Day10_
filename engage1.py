names = ("Haythem", "Mary", "Kate", "John", "Marcos") #we create a tuple object
print(type(names))
print(names)

my_iterator =  iter(names) # we use iter to create an iterable object

print(next(my_iterator)) # we use next to iterate through the tuple and print each name individually
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
