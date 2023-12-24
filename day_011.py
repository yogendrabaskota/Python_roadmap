#strings in python

name = "yogendra"
friend = "sujan"
# apple = " hi
#            hello"   it gives error
apple = ''' this is used for 
multiple line strings'''

print(apple)
print("hello " + name)
print(friend[0]) # print first letter of friend
#   print(friend[5])  gives index error

print("using for loop\n")

for character in name:
    print(character)