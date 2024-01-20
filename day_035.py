# for loop with else in python

for i in range(5):
    print(i)
else:
    print("sorry!")  # value of else is print after finished executing for loop

for j in []:
    print(j)
else:
    print("Thank you") # loop is empty, so directly printed this 


for k in range(6):
    print(k)
    if k == 4:
        break # terminate the loop
else:
    print("done") # content of else is not printed, because the loop is already terminated 


# same in while loop too
    