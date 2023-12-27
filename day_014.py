# if-else statement
a = int(input("enter your age \n"))
print("your age is: ", a)
if(a>18): 
    print("\nyou can drive")
else:
    print("\nyou can't drive")
print("\n\n")




appleprice = 200
budget = int(input("enter your budget\n"))
if(appleprice <= budget):
    print("\nyou can buy apple\n")
else:
    print("you can't buy apple\n")
print("\n\n")



#else-if
num = int(input("enter the value\n"))
if(num < 0):
    print("\nnumber is negative")
elif(num == 0):
    print("\nnumber is zero")
else:
    print("\nnumber is positive")
print("\n\n")


# nested if
n1 = int(input("enter the value\n"))
if(n1 < 0):
    print("\nnumber is negative")
elif(n1 > 0):
    if(n1 <= 10):
        print("\nnumber is between 1-10")
    elif(n1 > 10 and n1 <=20):
        print("\nnumber is between 10-20")
    else:
        print("\nnumber is greater than 20")
else:
    print("\nnumber is zero")

