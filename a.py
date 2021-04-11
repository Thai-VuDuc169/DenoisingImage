# A Python program to demonstrate packing of
# dictionary items using **
def fun(**kwargs):

	# kwargs is a dict
	print(type(kwargs))

	# Printing dictionary items
	for key in kwargs:
		print("%s = %s" % (key, kwargs[key]))

# Driver code
fun(name="geeks", ID="101", language="Python")
