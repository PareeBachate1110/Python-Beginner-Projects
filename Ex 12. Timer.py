#Experiment 12: Timer Program

import time

alarm=int(input("Enter Time in Seconds: "))

for x in range(1,alarm+1):
    time.sleep(1)
    print(x)

print("TIME'S UP!")

time.sleep(1)

print("NOW REVERSED!")
for x in reversed(range(1,alarm+1)):
    time.sleep(1)
    print(x)

print("TIME'S UP!")