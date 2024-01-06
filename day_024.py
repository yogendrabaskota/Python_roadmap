# tuple in pythoon
tup = (1,)  # , is necessary for tuple which have single item. 
print(tup)

tup1 = (1,2,3,43,57,"red")
print(type(tup),tup1)

print("index 0 :",tup1[0])
print("index 3 :",tup1[3])

a = input("enter number/item to be check ")

if a in tup1:
    print(a," is there in tuple")
else:
    print(a," is not available in tuple")

# tuples, are ordered, unchangeable collections of data items.
# Tuples use round brackets () and support positive and negative indexing, as well as checking for items using the 'in' keyword.
# It can also access items within a specific range or print alternate values using start, end, and jump index parameters.
# Tuples offer an efficient way to store multiple items in a single variable, while maintaining their order and immutability.
