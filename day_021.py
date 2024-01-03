# functions argument

def average(a,b):
    print("the average value is: ", (a+b)/2)
    
average(4,6)

# default argument:
def average1(a=10,b=20):  
    print("the average value is: ", (a+b)/2)
average1()   # no need any argument while calling the function. because we already given the value while declaring the function. so it takes default valur while calling
average1(6,8)  # it ignore the default value a=10 and b=20 and gives the average of 6 and 8 i.e 7
average1(2) # takes the value of a as 2 and default value if b i.e 20 and gives output 11


# keyword argument = order in which the arguments are passed does not matter.
average1(b=22,a=18) # no need to give  value in order
average1(b=20)  #takes default value of a i.e 10 and value of b as 20.

# Required arguments
def average2(a,b=20):  
    print("the average value is: ", (a+b)/2)
#average2() # it gives error because value of a is required and value of b is optional. if you give the value of b, it takes it and if not given it takes default value of b. but value of a is most
average2(100) #takes a=60
average2(22,24) # a=22 b=24



