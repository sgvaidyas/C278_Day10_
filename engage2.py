names_list = ["Haythem", "Mary", "Kate", "John", "Marcos"]
names_list_iterator  =  iter(names_list)
print("list iterator")
print(next(names_list_iterator))
print(next(names_list_iterator))
print("set iterator")
names_set = {"Haythem", "Mary", "Kate", "John", "Marcos"}
names_set_iterator  =  iter(names_set)
print(next(names_set_iterator))
print(next(names_set_iterator))
