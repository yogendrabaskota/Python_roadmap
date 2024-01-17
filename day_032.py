# Sets method in python
#union
s1 = {1,2,3,4}
s2 = {4,7,8}

print(s1.union(s2))  # print union of a1 and s2
print(s1,s2)  # union doesn't change their original values

print(s1.union(s2))
s1.update(s2) # update the value of s1 by the value of union
print(s1,s2)

#intersection
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

#symmetric difference = (A UNION B) - ( A INTERSECTION B)
cities4 = cities.symmetric_difference(cities2)
print(cities4)

# difference
cities5 = cities.difference(cities2)
print(cities5)

#methods
# isdisjoint()
print(cities.isdisjoint(cities2))  # print false, because they are not a disjoint set
# issuperset()
print(cities.issuperset(cities2))  # print false because cities is not a superaet of cities 2
# issubset 
print(cities.issubset(cities2)) # just a reverse of superset

# add()
# if you want to add a single item to the set use add() method 
cities.add("masko") # masko is added to the set cities
print(cities)
# update()  
# remove()/ discard() = remove item from the sets

cities.remove("masko")
print(cities)
# main difference between remove and discard is that if we try to deleete an item which is not present in set, then remove() raises an error , whereas discard() doesnot raise any error

# pop()
# This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

cities7 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities7.pop()
print(cities7)
print(item)

# clear()
# This method clears all items in the set and prints an empty set.
cities7.clear()
print(cities7)

# if statement in sets

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
    

