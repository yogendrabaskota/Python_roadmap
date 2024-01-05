# List methods in Python
l = [1,11,1,2,1,50,2,3,4,6]
print(l)

l.append(7) # adding 7 to list l
print(l)

l.sort() # sorting in ascending order
print(l) 

l.sort(reverse=True) # sorting in descending order
print(l)

print(l.index(3)) #  gives index of 3 i.e 5

print(l.count(1)) #count the number of occurance of enteredd value i.e 1

# m = l
# m[0] = 0 # first value of not only m but also l is changed to 0
# print(l) # gives the changed value

m = l.copy()
m[3] = 1 # third index of only m is changed l remain same
print(l)
print(m)

l.insert(1,899) # add 899 in index 1
print(l)

t = [1000, 2000, 3000]
l.extend(t) # adding values of t at the end of list l
print(l)


