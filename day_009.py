# Typecasting

# The conversion of one data type into the other data type is known as type casting in python

a = "1"
b = "2"
print(a+b)   # gives output 12
print(int(a) + int(b))   # gives output 3


print("\nProgram 2:\n")
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)