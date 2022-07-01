# Here is an example of a python inbuilt iterator
# value can be anything which can be iterate
iterable_value = 'PYTHON'
iterable_obj = iter(iterable_value)

while True:
	try:
		# Iterate by calling next
		item = next(iterable_obj)
		print(item)
	except StopIteration:
		# exception will happen when iteration will over
		break
