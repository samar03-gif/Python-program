#wap to create a dictionary taking input from user
strs = input("Enter key values pairs: ")

d = dict(x.split() for x in strs.splitlines())

print(d)
