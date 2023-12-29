# match case
x = int(input("enter value of x"))
match x:
    case 0:
        print("value of x is zero")
    case 5:
        print("value of x is 5")
    case 10:
        print("value of x is 10")
    case _ if(x != 80):
        print(x,"is not 80")
    case _ :  #default case
        print("value of x is ", x)
    
    
