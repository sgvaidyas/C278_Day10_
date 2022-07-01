names_dict = {"first_name":"Haythem", "last_name":"Balti"}

names_iterator  =  iter(names_dict)
print(next(names_iterator))
print(next(names_iterator))

names2 = iter(names_dict.items())
print(next(names2))
print(next(names2))

names3 = iter(names_dict.values())
print(next(names3))
print(next(names3))
