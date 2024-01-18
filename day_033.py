# Dictionaries in python
dic = {
    "Ram": "Ram is a lord of Hindus",
    "ravan": "ravan is not a god" 
}

print(dic["Ram"]) # print the values stored in name "Ram" i.e Ram is a lord of hindus
# we can map a employee id to employee name or similar to this kinds of works using dictionary in python
# Dictionary used for creating mapping between two 

dict = {
    1: "johns",
    2: "doy",
    3: "harry",
    4: "mark",
    5: "neumann"
}
print(dict[3])  # print the name of the person corresponding to number(ID) 3
print(dict) # print the whole dictionary

# print(dict[7])  # key "7" doesnot exist in dictionary so it throw error
print(dict.get(7)) # 7 doesnot exist in dictionary eventhough it prints "none" rather than throwing error message it is difference between using .get and not using it

print(dict.keys()) # prints all the keys i.e 1,2,3,4,5
print(dict.values()) # print all the values coprresponding to keys 

print("\nusing for loop:")
for key in dict.keys():
    print(dict[key])  # print values corresponding to keys

print("\n")
print(dict.items()) # print keys and values in pair






