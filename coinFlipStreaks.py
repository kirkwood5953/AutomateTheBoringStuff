# Write your code here :-)
import random
numOfStreaks = 0
streak = 0

n = 10000
for experimentNumber in range(n):
    #Create list of 100 H and T. 0 = H, 1 = T
    records = []
    for i in range(100):
        records.append(random.randint(0,1))
    #print(records)

    #Checks for presence of a streak
    for i in range(99):
        if records[i] == records[i+1]:
            streak += 1
        else:
            streak = 0

        if streak == 6:
            numOfStreaks += 1
   # print(numOfStreaks)

print('Chance of streak: %s%%' % (numOfStreaks / 100))
