# functions in python

def calculategmean(a,b):  #def is used for creating function(i.e user defined function)
    mean = (a*b)/(a+b)
    print(mean)
def great(a,b):
    if(a>=b):
        print("a is greater or equal")
    else:
        print("b is greater ")


a = 9
b = 8
# gmean = (a*b)/(a+b)
# print(gmean)
calculategmean(a,b) # can easy done using function. no need to repeat same formula again and again.
great(a,b)


c = 10
d = 20
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculategmean(c,d)
great(c,d)

# def islesser(a,b):  
    #nothing in body 
# gives error because function need to have its body

def islesser(a,b):
    pass  #pass means go ahead, and will finish later. no error


# RULES TO NAMING FUNCTION IS SIMILAR TO VARIABLES

# syntax of user defined function:
# def function_name(parameters):
#   pass  #code and statement
#
#