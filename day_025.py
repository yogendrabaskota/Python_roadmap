# Operations on tuple
# we can manupulate list but not tuple.
# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China", "India")
southEastAsia = countries + countries2
print(southEastAsia)
a = countries2.count("India")
# The count() method of Tuple returns the number of times the given element appears in the tuple.
print("country2 has ", a , " numbers of 'india' elements")

# The Index() method returns the first occurrence of the given element from the tuple.
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is at index ', res)
