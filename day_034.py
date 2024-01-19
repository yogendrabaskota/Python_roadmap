# Dictionary methods in python
ep1 = {110: 45, 123: 67, 456: 78, 344: 89}
ep2 = {333:66, 555: 56 }

ep1.update(ep2) #update ep1 dictionary by adding item of ep2 too
print(ep1)
# sets are unordered in python whereas dictionary are ordered

ep1.pop(110) # poping out(removing) key-value pair from dictionary
print(ep1)

ep1.popitem() # remove last key-value pair. i.e 555: 56 for now
print(ep1)

ep1.clear() # clear the dictionary ep1
print(ep1) # display empty dictionary because ep1 dictionary is cleared




