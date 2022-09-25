#python program to take tuple input in python

values = input('Please enter some values:')

#spliting the input values by space
input_tuple = tuple(int(val) for val in values.split())

print('tuple:',input_tuple)
