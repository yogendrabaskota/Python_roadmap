import time
timestamp = time.strftime('%H:%M:%S')
print("current time is ", timestamp)

timestamp1 = int(time.strftime('%H'))
print(timestamp1)

# timestamp2 = time.strftime('%M')
# print(timestamp2)
# 
# timestamp3 = time.strftime('%S')
# print(timestamp3)

if(timestamp1 < 12):
    print("good Morning")
elif(timestamp1 > 12):
    print("goodAfternoon")
else:
    print("noon")
