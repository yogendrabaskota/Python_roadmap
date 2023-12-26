a = "yogendra"

print(len(a))
print("\n")

#strings are immutable
print(a.upper())   #it makes new string (with strings in a) with all uppercase
print(a.lower())  # it makes new string with all lowercase in a
print("\n")

#rstrip
b = "john!!!!!!!!!!"

print(b)
print(b.rstrip("!")) #striping ! from string
print("\n")

#replace()

print(b.replace("john", "harry")) #replace john by harry and gives output as harry!!!!!!!!!!!
print("\n")

#split()
c = "ram    shyam hari ram"
print(c.split(" "))  #split is used to splits the given string at the specified instances and return the seperated strings as list item.
print("\n")

#capitalized()
#used to make first letter capital and others lowers
heading = "introduction tO pYTHon"
print(heading.capitalize())
print("\n")

#center()
print(heading.center(100)) #display heading in center
print("\n")

#count()
print(c.count("ram")) #give output 2 because there are 2 ram in string c
print("\n")

#endswith()
#it checks if the string ends with a given value or not. if yes, then return true, otherwise return false
print(b.endswith("!")) # gives true because string b ends with !
print("\n")
# we can even also check for a value in between the string by providing start and end index position

print(heading.endswith("on",2,12))
print("\n")
#gives true because 'troduction' ends with on

#find()
# gives index value of what we trying to find
g = "my name is yogendra baskota. yogendra is 20 years old."
print(g.find("yogendra"))
print("\n")
# gives 11 because index value of first occurance of yogendra i.e y is at 11th position .

#index()
#same as find but only difference is it gives error when we trying to find the string which is not available, whereas find gives -1 as output when string is not available 

#isalnum()
# this isalnum() method returns true only if the entire string only consist of A-Z, a-z, 0-9 i.e alphanumeric keys. if any others punctuations are present, then it returns false.
print(b.isalnum()) #false because ! i.e punctuation is present
print(c.isalnum()) #false because of space 
print(a.isalnum()) #true
print("\n")

#isalpha()
# if we remove 0-9 numbers from #isalnum(), it becomes #isalpha()




#islower()
#it returns true only if all the characters in the string are in lower case, otherwise retuen false.
print(a.islower()) #true
print(heading.islower()) #false
print("\n")

#isprintable()
#returns true if all the values within the given string are printable, if not then return false
print(a.isprintable()) #true
x = "\napple"
print(x.isprintable()) # false because \n is not printable
print("\n")

#isspace()
#true if string contain only whitespace, otherwise retuen false
z = "   "
print(a.isspace()) #false
print(z.isspace()) #true
print("\n")

#istitle()
# true only if the first letter of each word of the string is capitalized, else return false.
z = "International Cricket Counsil"
print(z.istitle()) #true
print("\n")

#isupper()
#opposite of islower()

#startswith()
#exactly as endswith()

#swapcase()
print(z.swapcase())
print("\n")
#swap the case i.e uppercase to lowercae and lowercase to uppercase.

#title()
#capitalized first letter of the word within the string
print(c.title())
print("\n")








